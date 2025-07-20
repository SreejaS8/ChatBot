import streamlit as st
import os
from datetime import datetime, timedelta
from groq import Groq
from ui import apply_custom_css, render_message
import json

# --- Page Setup ---
st.set_page_config(page_title="Groq Chatbot", layout="centered")
apply_custom_css()

# --- Load API Key ---
try:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except Exception:
    st.error("🔐 API Key not found.")
    st.stop()

# --- Logging Setup ---
def get_log_filename():
    folder = "chat_logs"
    os.makedirs(folder, exist_ok=True)
    # Use the date when the session started for log filename
    date_str = st.session_state.start_time.strftime("%Y-%m-%d")
    return os.path.join(folder, f"chatlog_{date_str}.jsonl")

def log_message(role, content):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "content": content
    }
    with open(get_log_filename(), "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

# --- Initialize Session Memory ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
    st.session_state.start_time = datetime.now()
    st.session_state.last_saved_log_date = st.session_state.start_time.date()

# --- Memory and Log Cleanup after 24hrs ---
if "start_time" in st.session_state:
    if datetime.now() - st.session_state.start_time > timedelta(hours=24):
        # Reset chat history and update start_time
        st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
        st.session_state.start_time = datetime.now()
        st.session_state.last_saved_log_date = st.session_state.start_time.date()

# --- Function to Get Response from Groq ---
def ask_groq():
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=st.session_state.messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# --- Display Chat UI ---
def main():
    # Scrollable chat area
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state.messages[1:]:
        role = "You" if msg["role"] == "user" else "Bot"
        render_message(role, msg["content"])
    st.markdown('</div>', unsafe_allow_html=True)

    # Sticky input bar
    st.markdown('<div class="input-bar">', unsafe_allow_html=True)
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("You:", placeholder="Type your message...")
        submitted = st.form_submit_button("Send")
    st.markdown('</div>', unsafe_allow_html=True)

    if submitted and user_input:
        # Log user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        log_message("user", user_input)

        # Get bot reply and log it
        bot_reply = ask_groq()
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        log_message("assistant", bot_reply)
        st.rerun()

# --- Run ---
if __name__ == "__main__":
    main()