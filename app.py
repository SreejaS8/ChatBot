# app.py

import streamlit as st
from groq import Groq
import os

# ⛳ Set page configuration with custom favicon
favicon_path = "assets/groq_logo.png"
if os.path.exists(favicon_path):
    st.set_page_config(page_title="Groq Chatbot", page_icon=favicon_path, layout="wide")
else:
    st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="wide")

# 🖼️ Display logo if available
if os.path.exists(favicon_path):
    st.image(favicon_path, width=100)
else:
    st.warning("Logo image not found. Displaying default emoji instead.")

# 🎨 Page styling
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>Chat with LLaMA3 💬</h1>", unsafe_allow_html=True)
st.caption("Powered by Groq + Streamlit")
st.markdown("<hr>", unsafe_allow_html=True)

# 🔐 Load Groq API key securely from secrets
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# 💬 Function to interact with Groq model
def ask_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"

# 🧠 Initialize session chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [("System", "Hi! I'm your Groq-powered chatbot. Say something!")]

# 🗣️ Input form
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([6, 1])
    with col1:
        user_input = st.text_input("Type your message:")
    with col2:
        submitted = st.form_submit_button("Send")

# 📥 Handle input
if submitted and user_input:
    st.session_state.chat_history.append(("You", user_input))
    bot_reply = ask_groq(user_input)
    st.session_state.chat_history.append(("Bot", bot_reply))

# 💬 Display chat messages with styled bubbles
for sender, message in st.session_state.chat_history:
    color = "#EEE"
    if sender == "You":
        color = "#DCF8C6"
    elif sender == "Bot":
        color = "#F1F0F0"

    st.markdown(
        f"<div style='background-color:{color};padding:10px;border-radius:10px;margin-bottom:5px'>"
        f"<strong>{sender}:</strong> {message}</div>",
        unsafe_allow_html=True
    )