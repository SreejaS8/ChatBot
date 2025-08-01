import streamlit as st
import os
from datetime import datetime, timedelta
from groq import Groq
from ui import apply_custom_css, render_message, show_typing_indicator, render_startup_intro, render_title_corner
import json
import time

# --- Page Setup ---
st.set_page_config(
    page_title="SuperLaw - Legal Assistant", 
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply stunning CSS
apply_custom_css()

# --- Log Function ---
def log_message(role, content):
    """Log messages to local file"""
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
        # Write to local file
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
            
    except Exception as e:
        st.error(f"Logging error: {str(e)}")

# --- Load API Key from Streamlit Secrets ---
try:
    # Get API key from Streamlit secrets
    api_key = st.secrets["GROQ_API_KEY"]
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in secrets")
    
    client = Groq(api_key=api_key)
    
except Exception as e:
    st.error("🔐 **Groq API Key not found in Streamlit secrets!**")
    st.info("""
    **Setup Instructions:**
    1. Go to your Streamlit app settings
    2. Add to secrets.toml:
    ```toml
    GROQ_API_KEY = "your_groq_api_key_here"
    ```
    """)
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
    
    if "user_ip" not in st.session_state:
        # Try to get user IP (limited in Streamlit Cloud)
        st.session_state.user_ip = "local"
    
    if "daily_message_count" not in st.session_state:
        st.session_state.daily_message_count = 0
    
    if "last_log_date" not in st.session_state:
        st.session_state.last_log_date = datetime.now().date()

# --- Memory Cleanup and Log Management (24-hour reset) ---
def check_session_reset():
    """Reset session after 24 hours"""
    current_date = datetime.now().date()
    
    if "start_time" in st.session_state:
        if datetime.now() - st.session_state.start_time > timedelta(hours=24):
            # Reset session
            st.session_state.messages = [
                {"role": "system", "content": "You are SuperLaw AI, a highly knowledgeable and helpful legal assistant. Provide accurate, clear, and professional legal information while always reminding users to consult with qualified attorneys for specific legal advice."}
            ]
            st.session_state.start_time = datetime.now()
            st.session_state.session_id = f"session_{int(time.time())}"
            st.session_state.daily_message_count = 0
            st.session_state.last_log_date = current_date
            st.success("🔄 Session refreshed after 24 hours")
    
    # Check if date changed (new day)
    if st.session_state.last_log_date != current_date:
        st.session_state.daily_message_count = 0
        st.session_state.last_log_date = current_date

def get_log_file_info():
    """Get information about log files"""
    folder = "chat_logs"
    if not os.path.exists(folder):
        return []
    
    log_files = []
    for filename in os.listdir(folder):
        if filename.startswith("superlaw_chatlog_") and filename.endswith(".jsonl"):
            file_path = os.path.join(folder, filename)
            file_size = os.path.getsize(file_path)
            file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
            log_files.append({
                'name': filename,
                'size': file_size,
                'modified': file_modified,
                'path': file_path
            })
    
    return sorted(log_files, key=lambda x: x['modified'], reverse=True)

def clean_old_logs(days_to_keep=7):
    """Clean log files older than specified days"""
    folder = "chat_logs"
    if not os.path.exists(folder):
        return 0
    
    cutoff_date = datetime.now() - timedelta(days=days_to_keep)
    cleaned_count = 0
    
    try:
        for filename in os.listdir(folder):
            if filename.startswith("superlaw_chatlog_") and filename.endswith(".jsonl"):
                file_path = os.path.join(folder, filename)
                file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
                
                if file_modified < cutoff_date:
                    os.remove(file_path)
                    cleaned_count += 1
    except Exception as e:
        st.error(f"Error cleaning old logs: {str(e)}")
    
    return cleaned_count

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
    
    # Show dramatic startup intro animation
    render_startup_intro()
    
    # Wrap main content for animation
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Render title after animation
    render_title_corner()
    
    # Sidebar info
    with st.sidebar:
        st.markdown("### 📊 Session Info")
        st.info(f"**Session:** {st.session_state.session_id[:12]}...")
        st.info(f"**Started:** {st.session_state.start_time.strftime('%H:%M:%S')}")
        st.info(f"**Messages:** {len(st.session_state.messages) - 1}")
        st.info(f"**Daily Count:** {st.session_state.daily_message_count}")
        
        if st.button("🔄 Reset Chat"):
            st.session_state.messages = [st.session_state.messages[0]]  # Keep system message
            st.rerun()
        
        st.markdown("---")
        
        # Log Management Section
        st.markdown("### 📝 Log Management")
        log_files = get_log_file_info()
        
        if log_files:
            st.success(f"📁 {len(log_files)} log files found")
            
            # Show current day's log info
            today_log = next((f for f in log_files if datetime.now().strftime('%Y-%m-%d') in f['name']), None)
            if today_log:
                st.info(f"**Today's log:** {today_log['size']} bytes")
            
            # Clean old logs button
            if st.button("🧹 Clean Old Logs (7+ days)"):
                cleaned = clean_old_logs(7)
                if cleaned > 0:
                    st.success(f"✅ Cleaned {cleaned} old log files")
                else:
                    st.info("No old log files to clean")
                st.rerun()
            
            # Show log files info
            with st.expander("📋 Log Files Details"):
                for log_file in log_files[:5]:  # Show last 5 files
                    st.text(f"📄 {log_file['name']}")
                    st.text(f"   Size: {log_file['size']} bytes")
                    st.text(f"   Modified: {log_file['modified'].strftime('%Y-%m-%d %H:%M:%S')}")
                    st.text("---")
        else:
            st.info("📁 No log files found yet")
        
        st.markdown("---")
        st.markdown("### ⚖️ About SuperLaw")
        st.markdown("""
        Your intelligent legal assistant powered by advanced AI. 
        
        **Features:**
        - 🧠 Advanced legal knowledge
        - 📝 Document analysis
        - 🔍 Case law research
        - ⚡ Instant responses
        - 💾 Local chat logging
        
        **Disclaimer:** Always consult qualified attorneys for legal advice.
        """)
        
        st.markdown("---")
        st.markdown("### 🔒 Privacy & Logs")
        st.markdown("""
        - 📝 Conversations logged locally
        - 💾 Stored in `/chat_logs` folder
        - 🔄 24-hour auto session reset
        - 🧹 Auto-cleanup old logs
        - 🔐 All data stays on your server
        """)
    
    # Chat container
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Display chat messages
    for msg in st.session_state.messages[1:]:  # Skip system message
        role = "You" if msg["role"] == "user" else "SuperLaw AI"
        render_message(role, msg["content"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Input form
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
    
    # Process user input
    if submitted and user_input and not st.session_state.is_processing:
        st.session_state.is_processing = True
        st.session_state.daily_message_count += 1
        
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