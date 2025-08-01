import streamlit as st
import os
from datetime import datetime, timedelta
from groq import Groq
from ui import apply_custom_css, render_message, render_startup_intro, render_title_corner
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

# --- Log Function ---
def log_message(role, content):
    """Log messages to a local file for history and debugging"""
    folder = "chat_logs"
    os.makedirs(folder, exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d')
    log_path = os.path.join(folder, f"superlaw_chatlog_{date_str}.jsonl")
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "content": content,
        "session_id": st.session_state.get('session_id', 'unknown'),
        "user_ip": st.session_state.get('user_ip', 'local')
    }
    
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
            
    except Exception as e:
        st.error(f"Logging error: {str(e)}")

# --- Load API Key from Streamlit Secrets ---
try:
    api_key = st.secrets["GROQ_API_KEY"]
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in secrets")
    
    client = Groq(api_key=api_key)
    
except Exception as e:
    st.error("🔐 **Groq API Key not found in Streamlit secrets!**")
    st.info("""
    **Setup Instructions:**
    1. Go to your Streamlit app settings.
    2. Add to a file named `.streamlit/secrets.toml`:
    ```toml
    GROQ_API_KEY = "your_groq_api_key_here"
    ```
    """)
    st.stop()

# --- Initialize Session State ---
def initialize_session():
    """Initialize all necessary session state variables"""
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
    # Initialize session state
    initialize_session()
    
    # Show dramatic startup intro animation
    render_startup_intro()
    
    # Render the fixed title
    render_title_corner()
    
    # Sidebar info and controls
    with st.sidebar:
        st.markdown("### 📊 Session Info")
        st.info(f"**Session:** {st.session_state.session_id[:12]}...")
        st.info(f"**Started:** {st.session_state.start_time.strftime('%H:%M:%S')}")
        st.info(f"**Messages:** {len(st.session_state.messages) - 1}")
        
        if st.button("🔄 Reset Chat"):
            # Keep the system message but clear the rest
            st.session_state.messages = [st.session_state.messages[0]]
            st.rerun()

    # Chat container for displaying messages
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Display all messages from session state, skipping the initial system message
    for msg in st.session_state.messages[1:]:
        role = "You" if msg["role"] == "user" else "SuperLaw AI"
        render_message(role, msg["content"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # The input form for the user
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
    
    # Process user input on form submission
    if submitted and user_input and not st.session_state.is_processing:
        st.session_state.is_processing = True
        
        # Add the user's message to the chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        log_message("user", user_input)
        
        # Get and add the AI's response
        ai_response = get_ai_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        log_message("assistant", ai_response)
        
        st.session_state.is_processing = False
        st.rerun()

# --- Run the app ---
if __name__ == "__main__":
    main()