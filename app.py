import streamlit as st
from groq import Groq
import os

# Load Groq API Key from Streamlit secrets
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Function to call Groq model
def ask_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"

# UI setup
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("💬 Chat with LLaMA3 (Groq)")
st.caption("Powered by Groq + Streamlit")

# Chat history initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [("System", "Hi! I'm your Groq-powered chatbot. Say something!")]

# Input text box
user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    bot_reply = ask_groq(user_input)
    st.session_state.chat_history.append(("Bot", bot_reply))
    st.session_state.user_input = ""

# Chat display
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
