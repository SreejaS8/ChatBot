import streamlit as st
import time
from datetime import datetime, timedelta
from ui import apply_custom_css, render_message, render_title_area

# --- Main App Logic ---

# Set Streamlit page configuration
st.set_page_config(
    page_title="SuperLaw - Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply the custom CSS
apply_custom_css()

# Render the title area
render_title_area()

# Initialize chat session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am SuperLaw, your legal assistant. How can I help you today?"}
    ]

# Display chat messages
for msg in st.session_state.messages:
    render_message(msg["role"], msg["content"])

# Input area fixed at the bottom
st.markdown('<div class="fixed-bottom">', unsafe_allow_html=True)
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
        submitted = st.form_submit_button("Send 🚀", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Handle user input and generate a response
if submitted and user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Simulate a bot response for this simple example
    with st.spinner('SuperLaw AI is thinking...'):
        time.sleep(2)  # Simulate API call delay
        
    # Add the bot's response to chat history
    st.session_state.messages.append({"role": "assistant", "content": f"You said: {user_input}"})
    
    # Rerun the app to update the display with the new messages
    st.rerun()
