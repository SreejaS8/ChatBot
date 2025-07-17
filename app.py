import streamlit as st
from groq import Groq
import os

# Page configuration
favicon_path = "assets/groq_logo.png"
if os.path.exists(favicon_path):
    st.set_page_config(page_title="Image Agent+", page_icon=favicon_path, layout="wide")
else:
    st.set_page_config(page_title="Image Agent+", page_icon="🤖", layout="wide")

# Groq API key
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Summarization trigger
if "start_chat" not in st.session_state:
    st.session_state.start_chat = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to interact with Groq model
def ask_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"

# Layout: two columns side by side
left, right = st.columns([1, 2])

# 🔮 LEFT PANEL — START Button and Branding
with left:
    if os.path.exists(favicon_path):
        st.image(favicon_path, width=80)
    st.markdown("<h2 style='color:#6C63FF;'>Bot by Sree</h2>", unsafe_allow_html=True)
    st.markdown("Click below to start summarizing images or chat with your AI agent.")
    start_btn = st.button("🚀 START SUMMARIZING")

    if start_btn:
        st.session_state.start_chat = True

# 💬 RIGHT PANEL — Chat Interface (only when activated)
with right:
    if st.session_state.start_chat:
        st.markdown("<h4 style='color:gray;'>New Chat</h4>", unsafe_allow_html=True)
        st.markdown("<div style='background-color:#F1F0F0;padding:10px;border-radius:10px;margin-bottom:10px'>"
                    "Hi, I'm your AI agent! Send an image or type a message below.</div>",
                    unsafe_allow_html=True)

        # Chat input
        with st.form("chat_form", clear_on_submit=True):
            col1, col2 = st.columns([6, 1])
            with col1:
                user_input = st.text_input("Start typing...")
            with col2:
                submitted = st.form_submit_button("Send")

        if submitted and user_input:
            st.session_state.chat_history.append(("You", user_input))
            bot_reply = ask_groq(user_input)
            st.session_state.chat_history.append(("Bot", bot_reply))

        # Show chat history
        for sender, message in st.session_state.chat_history:
            bubble_color = "#DCF8C6" if sender == "You" else "#F1F0F0"
            st.markdown(
                f"<div style='background-color:{bubble_color};padding:10px;border-radius:10px;margin-bottom:5px'>"
                f"<strong>{sender}:</strong> {message}</div>",
                unsafe_allow_html=True
            )
    else:
        st.markdown("<div style='text-align:center;color:gray;padding-top:50px;'>"
                    "<em>Chat will appear here once you press 'START SUMMARIZING'</em></div>",
                    unsafe_allow_html=True)