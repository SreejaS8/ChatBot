# app.py

import streamlit as st
from groq import Groq
import os

# ⛳ Set page configuration with custom favicon
st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="assets/groq_logo.png",  # Custom favicon
    layout="wide"
)

# 🖼️ Display your logo
st.image("assets/groq_logo.png", width=100)
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>Chat with LLaMA3 💬</h1>", unsafe_allow_html=True)
st.caption("Powered by Groq + Streamlit")
st.markdown("<hr>", unsafe_allow_html=True)

# 🔐 Load Groq API key securely from secrets
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# 💬 Function to call Groq model
def ask_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"

# 🧠 Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [("System", "Hi! I'm your Groq-powered chatbot. Say something!")]

# 🧾 Chat input form
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([6, 1])
    with col1:
        user_input = st.text_input("Type your message:")
    with col2:
        submitted = st.form_submit_button("Send")

# 🤖 Handle user input
if submitted and user_input:
    st.session_state.chat_history.append(("You", user_input))
    bot_reply = ask_groq(user_input)
    st.session_state.chat_history.append(("Bot", bot_reply))

# 🌈 Display chat with custom UI styling
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(
            f"<div style='background-color:#DCF8C6;padding:10px;border-radius:10px;margin-bottom:5px'>"
            f"<strong>You:</strong> {message}</div>",
            unsafe_allow_html=True
        )
    elif sender == "Bot":
        st.markdown(
            f"<div style='background-color:#F1F0F0;padding:10px;border-radius:10px;margin-bottom:5px'>"
            f"<strong>Bot:</strong> {message}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#EEE;padding:10px;border-radius:10px;margin-bottom:5px'>"
            f"<strong>{sender}:</strong> {message}</div>",
            unsafe_allow_html=True
        )