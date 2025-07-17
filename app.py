import streamlit as st
from groq import Groq
import os
import time
from ui import (
    apply_custom_css, 
    render_header, 
    render_chat_history, 
    render_input_area, 
    render_sidebar,
    render_typing_indicator,
    show_error_message,
    initialize_session_state
)

# Page configuration
st.set_page_config(
    page_title="Groq Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Groq API Key from Streamlit secrets
try:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except Exception as e:
    st.error("❌ Failed to load Groq API key. Please check your Streamlit secrets.")
    st.stop()

def ask_groq(prompt):
    """Call Groq model with error handling and typing simulation"""
    try:
        # Show typing indicator
        typing_placeholder = st.empty()
        with typing_placeholder.container():
            render_typing_indicator()
        
        # Simulate thinking time
        time.sleep(1)
        
        # Make API call
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096,
            temperature=0.7,
            stream=False
        )
        
        # Clear typing indicator
        typing_placeholder.empty()
        
        return response.choices[0].message.content
    
    except Exception as e:
        typing_placeholder.empty()
        return f"I apologize, but I encountered an error: {str(e)}"

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Apply custom CSS
    apply_custom_css()
    
    # Render sidebar
    render_sidebar()
    
    # Main content area
    with st.container():
        # Render header
        render_header()
        
        # Create main chat area
        chat_container = st.container()
        
        # Render input area
        user_input, send_button = render_input_area()
        
        # Handle form submission
        if send_button and user_input.strip():
            # Add user message to chat history
            st.session_state.chat_history.append(("You", user_input))
            
            # Get bot response
            with chat_container:
                bot_reply = ask_groq(user_input)
                
            # Add bot response to chat history
            st.session_state.chat_history.append(("Bot", bot_reply))
            
            # Clear input and rerun to show updated chat
            st.rerun()
        
        # Handle Enter key submission
        if user_input and not send_button:
            # This handles the case where user presses Enter in the text input
            if st.session_state.get("last_input") != user_input:
                st.session_state.last_input = user_input
        
        # Render chat history
        with chat_container:
            render_chat_history(st.session_state.chat_history)
    
    # Auto-scroll to bottom (JavaScript injection)
    st.markdown("""
    <script>
        setTimeout(function() {
            window.scrollTo(0, document.body.scrollHeight);
        }, 100);
    </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()