# app.py

import streamlit as st
from groq import Groq
import os
import time
from ui import (
    apply_custom_css,
    render_header,
    render_chat_messages,
    render_input_area,
    render_typing_indicator,
    initialize_session_state
)

st.set_page_config(
    page_title="AI Image Summarizer",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

try:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except:
    st.error("Failed to load Groq API key")
    st.stop()

def ask_groq(prompt):
    """Get response from Groq"""
    try:
        typing_placeholder = st.empty()
        with typing_placeholder.container():
            render_typing_indicator()
        
        time.sleep(1)
        
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096,
            temperature=0.7
        )
        
        typing_placeholder.empty()
        return response.choices[0].message.content
    
    except Exception as e:
        typing_placeholder.empty()
        return f"Error: {str(e)}"

def main():
    initialize_session_state()
    apply_custom_css()
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    render_header()
    
    chat_container = st.container()
    
    user_input, send_button = render_input_area()
    
    if send_button and user_input.strip():
        st.session_state.chat_history.append(("You", user_input))
        
        with chat_container:
            bot_reply = ask_groq(user_input)
            
        st.session_state.chat_history.append(("Bot", bot_reply))
        st.rerun()
    
    with chat_container:
        render_chat_messages(st.session_state.chat_history)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()