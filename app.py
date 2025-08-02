import streamlit as st
import os
from datetime import datetime, timedelta
from groq import Groq
from ui import apply_custom_css, render_message, render_startup_intro, render_title_area
import json
import time

# --- Page Setup ---
st.set_page_config(
    page_title="SuperLaw - Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply stunning CSS from ui.py
apply_custom_css()

# --- Initialize Session State for Intro ---
if "show_intro" not in st.session_state:
    st.session_state.show_intro = True

def hide_intro():
    """Callback function to hide the intro screen"""
    st.session_state.show_intro = False

# --- Placeholder for Google Drive Logging ---
def log_to_google_drive(folder_id, data):
    """
    Placeholder function to log data to a file in Google Drive.
    """
    try:
        print(f"Logging to Google Drive folder '{folder_id}':\n{data}\n---")
        return True
    except Exception as e:
        st.error(f"Failed to log to Google Drive: {e}")
        return False

def log_message(role, content, drive_folder_id):
    """Log messages to Google Drive for history and persistence"""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "content": content,
        "session_id": st.session_state.get('session_id', 'unknown')
    }
    
    log_to_google_drive(drive_folder_id, json.dumps(log_entry, ensure_ascii=False) + "\n")


# --- Load API Keys from Streamlit Secrets ---
try:
    api_key = st.secrets["GROQ_API_KEY"]
    drive_folder_id = st.secrets["DRIVE_LOG_FOLDER_ID"]
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in secrets")
    if not drive_folder_id:
        raise ValueError("DRIVE_LOG_FOLDER_ID not found in secrets")
    
    client = Groq(api_key=api_key)
    
except Exception as e:
    st.error("🔐 **Required secrets not found!**")
    st.info(f"""
    **Missing Secret**: {e}
    
    Please add the following to your `.streamlit/secrets.toml`:
    ```toml
    GROQ_API_KEY = "your_groq_api_key_here"
    DRIVE_LOG_FOLDER_ID = "your_google_drive_folder_id_here"
    ```
    """)
    st.stop()

# --- Initialize Session State for Chat ---
def initialize_chat_session():
    """Initialize all necessary session state variables for the chat"""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are SuperLaw AI, a highly knowledgeable and helpful legal assistant. Provide accurate, clear, and professional legal information while always reminding users to consult with qualified attorneys for specific legal advice."}
        ]
    
    if "start_time" not in st.session_state:
        st.session_state.start_time = datetime.now()
    
    if "session_id" not in st.session_state:
        st.session_state.session_id = f"session_{int(time.time())}"
    
    if "is_processing" not in st.session_state:
        st.session_state.is_processing = False

# --- Get AI Response ---
def get_ai_response(prompt_messages):
    """Get response from Groq AI"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=prompt_messages,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ **Error**: I encountered an issue: {str(e)}\n\nPlease try again in a moment."

# --- Main App ---
def main():
    if st.session_state.show_intro:
        # Show intro animation and a button to proceed
        render_startup_intro()
        st.markdown('<div class="fixed-bottom">', unsafe_allow_html=True)
        st.button("Enter App", on_click=hide_intro, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Main application logic
        initialize_chat_session()
        
        # Render the fixed title
        render_title_area()
        
        # Sidebar info and controls
        with st.sidebar:
            st.markdown("### 📊 Session Info")
            st.info(f"**Session ID:** {st.session_state.session_id[:12]}...")
            st.info(f"**Started:** {st.session_state.start_time.strftime('%H:%M:%S')}")
            st.info(f"**Messages:** {len(st.session_state.messages) - 1}")
            
            if st.button("🔄 Reset Chat"):
                st.session_state.messages = [st.session_state.messages[0]]
                st.rerun()

            st.markdown("---")
            st.markdown("### ⚖️ About SuperLaw")
            st.markdown("""
            Your intelligent legal assistant powered by advanced AI. 
            
            **Features:**
            - 🧠 Advanced legal knowledge
            - 📝 Document analysis
            - 🔍 Case law research
            - ⚡ Instant responses
            - 💾 Chat history logged to Google Drive
            
            **Disclaimer:** Always consult qualified attorneys for legal advice.
            """)

        # Chat container for displaying messages
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        for msg in st.session_state.messages[1:]:
            role = "You" if msg["role"] == "user" else "SuperLaw AI"
            render_message(role, msg["content"])
        
        st.markdown('</div>', unsafe_allow_html=True)

        # The input form fixed at the bottom of the page
        st.markdown('<div class="fixed-bottom">', unsafe_allow_html=True)
        with st.form("chat_form", clear_on_submit=True):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                user_input = st.text_input(
                    "Ask SuperLaw AI anything about law...",
                    placeholder="Type your legal question here...",
                    key="user_input",
                    label_visibility="collapsed"
                )
            
            with col2:
                submitted = st.form_submit_button(
                    "Send 🚀",
                    use_container_width=True,
                    disabled=st.session_state.is_processing
                )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Process user input on form submission
        if submitted and user_input and not st.session_state.is_processing:
            st.session_state.is_processing = True
            
            st.session_state.messages.append({"role": "user", "content": user_input})
            log_message("user", user_input, drive_folder_id)
            
            ai_response = get_ai_response(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            log_message("assistant", ai_response, drive_folder_id)
            
            st.session_state.is_processing = False
            st.rerun()

# --- Run the app ---
if __name__ == "__main__":
    main()