# app.py

import streamlit as st
from groq import Groq
import os
from ui import apply_custom_css, render_message, initialize_session_state

st.set_page_config(page_title="Chat Bot", layout="centered")

try:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except:
    st.error("Failed to load Groq API key")
    st.stop()

def ask_groq(prompt):
    """Get response from Groq"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    initialize_session_state()
    apply_custom_css()
    
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Display chat history
    for sender, message in st.session_state.chat_history:
        render_message(sender, message)
    
    # Input area
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your message:", placeholder="Ask me anything...")
        submitted = st.form_submit_button("Send")
    
    if submitted and user_input:
        st.session_state.chat_history.append(("You", user_input))
        bot_reply = ask_groq(user_input)
        st.session_state.chat_history.append(("Bot", bot_reply))
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()