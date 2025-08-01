import streamlit as st
import os
from datetime import datetime, timedelta
from groq import Groq
from ui import apply_custom_css, render_message, show_typing_indicator, render_startup_intro, render_title_corner
import json
import time
# from pydrive2.auth import GoogleAuth
# from pydrive2.drive import GoogleDrive

# ===== SET THE DRIVE FOLDER ID HERE =====
# DRIVE_LOG_FOLDER_ID = st.secrets.get("DRIVE_LOG_FOLDER_ID", "")

# --- Page Setup ---
st.set_page_config(
    page_title="SuperLaw - Legal Assistant", 
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply stunning CSS
apply_custom_css()

# --- Configure Google Drive Auth (Optional - uncomment if needed) ---
# def gdrive_authenticate():
#     gauth = GoogleAuth()
#     gauth.LocalWebserverAuth()
#     return GoogleDrive(gauth)

# def upload_log_to_drive(local_path, drive_folder_id):
#     if not drive_folder_id:
#         return
#     try:
#         drive = gdrive_authenticate()
#         file_drive = drive.CreateFile({'title': os.path.basename(local_path),
#                                        'parents': [{'id': drive_folder_id}]})
#         file_drive.SetContentFile(local_path)
#         file_drive.Upload()
#         st.success("✅ Log uploaded to Google Drive!")
#     except Exception as e:
#         st.error(f"❌ Failed to upload to Drive: {str(e)}")

# --- Log Function ---
def log_message(role, content):
    """Log messages to local file"""
    folder = "chat_logs"
    os.makedirs(folder, exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d')
    log_path = os.path.join(folder, f"chatlog_{date_str}.jsonl")
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "content": content,
        "session_id": st.session_state.get('session_id', 'unknown')
    }
    
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        st.error(f"Logging error: {str(e)}")

# --- Load API Key ---
try:
    # Try to get from secrets first, then environment
    api_key = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("API key not found")
    
    client = Groq(api_key=api_key)
    
except Exception as e:
    st.error("🔐 **Groq API Key not found!**")
    st.info("Please add your GROQ_API_KEY to Streamlit secrets or environment variables.")
    st.stop()

# --- Initialize Session State ---
def initialize_session():
    """Initialize session state variables"""
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

# --- Memory Cleanup (24-hour reset) ---
def check_session_reset():
    """Reset session after 24 hours"""
    if "start_time" in st.session_state:
        if datetime.now() - st.session_state.start_time > timedelta(hours=24):
            st.session_state.messages = [
                {"role": "system", "content": "You are SuperLaw AI, a highly knowledgeable and helpful legal assistant. Provide accurate, clear, and professional legal information while always reminding users to consult with qualified attorneys for specific legal advice."}
            ]
            st.session_state.start_time = datetime.now()
            st.session_state.session_id = f"session_{int(time.time())}"
            st.success("🔄 Session refreshed after 24 hours")

# --- Get AI Response ---
def get_ai_response():
    """Get response from Groq AI"""
    try:
        with st.spinner("🤖 SuperLaw is thinking..."):
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=st.session_state.messages,
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
    # Initialize session
    initialize_session()
    check_session_reset()
    
    # Show startup intro animation
    render_startup_intro()
    
    # Wrap main content for animation
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Render title in corner after animation
    render_title_corner()
    
    # Sidebar info
    with st.sidebar:
        st.markdown("### 📊 Session Info")
        st.info(f"**Session:** {st.session_state.session_id[:12]}...")
        st.info(f"**Started:** {st.session_state.start_time.strftime('%H:%M:%S')}")
        st.info(f"**Messages:** {len(st.session_state.messages) - 1}")
        
        if st.button("🔄 Reset Chat"):
            st.session_state.messages = [st.session_state.messages[0]]  # Keep system message
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
        
        **Disclaimer:** Always consult qualified attorneys for legal advice.
        """)
    
    # Chat container
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Display chat messages
    for msg in st.session_state.messages[1:]:  # Skip system message
        role = "You" if msg["role"] == "user" else "SuperLaw AI"
        render_message(role, msg["content"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Input form
    st.markdown('<div class="input-bar">', unsafe_allow_html=True)
    
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
    
    # Process user input
    if submitted and user_input and not st.session_state.is_processing:
        st.session_state.is_processing = True
        
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        log_message("user", user_input)
        
        # Get AI response
        ai_response = get_ai_response()
        
        # Add AI response
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        log_message("assistant", ai_response)
        
        st.session_state.is_processing = False
        st.rerun()
    
    # Close main content wrapper
    st.markdown('</div>', unsafe_allow_html=True)

# --- Run the app ---
if __name__ == "__main__":
    main()