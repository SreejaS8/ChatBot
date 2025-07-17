# app.py

import streamlit as st
import os
from datetime import datetime, timedelta
from groq import Groq
from ui import apply_custom_css, render_message

# --- Page Setup ---
st.set_page_config(page_title="Groq Chatbot", layout="centered")
apply_custom_css()

# --- Load API Key ---
try:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except:
    st.error("🔐 API Key not found.")
    st.stop()

# --- Initialize Session Memory ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
    st.session_state.start_time = datetime.now()

# --- Memory Cleanup after 24hrs ---
if "start_time" in st.session_state:
    if datetime.now() - st.session_state.start_time > timedelta(hours=24):
        st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
        st.session_state.start_time = datetime.now()

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
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Display messages
    for msg in st.session_state.messages[1:]:  # Skip system message
        role = "You" if msg["role"] == "user" else "Bot"
        render_message(role, msg["content"])

    # Chat input
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("You:", placeholder="Type your message...")
        submitted = st.form_submit_button("Send")

    if submitted and user_input:
        # Add user input to memory
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get bot reply
        bot_reply = ask_groq()
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# --- Run ---
if __name__ == "__main__":
    main()
