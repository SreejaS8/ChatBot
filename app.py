# app.py

import streamlit as st
import os
from groq import Groq
from ui import apply_custom_css, render_message, initialize_session_state

# --- Page setup ---
st.set_page_config(page_title="Groq Chatbot", layout="centered")
apply_custom_css()
initialize_session_state()

# --- Load API Key ---
try:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except Exception as e:
    st.error("🔐 API Key not found in secrets.")
    st.stop()

# --- Function to get model response ---
def ask_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# --- Main App ---
def main():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Show chat history
    for sender, message in st.session_state.chat_history:
        render_message(sender, message)

    # User input form
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("You:", placeholder="Type your message...")
        submitted = st.form_submit_button("Send")

    # On submit
    if submitted and user_input:
        st.session_state.chat_history.append(("You", user_input))
        bot_reply = ask_groq(user_input)
        st.session_state.chat_history.append(("Bot", bot_reply))
        st.rerun()  # Refresh the app to show the new messages

    st.markdown('</div>', unsafe_allow_html=True)

# --- Run ---
if __name__ == "__main__":
    main()
