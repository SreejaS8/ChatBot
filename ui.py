# ui.py

import streamlit as st
import base64
import os

def get_base64_image(image_path):
    """Convert image to base64 for CSS background"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def apply_custom_css():
    """Apply custom CSS to match the image design"""
    
    # Try to load background image from assets folder
    bg_image = get_base64_image("assets/background.jpg") or get_base64_image("assets/background.png")
    
    background_style = f"""
        background-image: url('data:image/jpeg;base64,{bg_image}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    """ if bg_image else """
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    """
    
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    .stApp {{
        {background_style}
    }}
    
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(10px);
        z-index: -1;
    }}
    
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{visibility: hidden;}}
    
    .main-container {{
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        height: 100vh;
        display: flex;
        flex-direction: column;
        font-family: 'Inter', sans-serif;
    }}
    
    .chat-header {{
        text-align: center;
        margin-bottom: 30px;
        position: relative;
    }}
    
    .new-chat-btn {{
        position: absolute;
        top: 0;
        right: 0;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 8px 16px;
        color: white;
        font-size: 12px;
        cursor: pointer;
        backdrop-filter: blur(10px);
    }}
    
    .chat-title {{
        color: white;
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 10px;
    }}
    
    .chat-messages {{
        flex: 1;
        overflow-y: auto;
        padding: 20px 0;
        scrollbar-width: none;
        -ms-overflow-style: none;
    }}
    
    .chat-messages::-webkit-scrollbar {{
        display: none;
    }}
    
    .message-bubble {{
        background: rgba(59, 130, 246, 0.9);
        color: white;
        padding: 12px 18px;
        border-radius: 20px;
        margin: 10px 0;
        max-width: 70%;
        margin-left: auto;
        margin-right: 0;
        font-size: 14px;
        line-height: 1.4;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(59, 130, 246, 0.3);
    }}
    
    .bot-message {{
        background: rgba(255, 255, 255, 0.1);
        color: white;
        margin-left: 0;
        margin-right: auto;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    
    .system-message {{
        background: rgba(34, 197, 94, 0.2);
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        margin: 0 auto;
        font-size: 13px;
        border: 1px solid rgba(34, 197, 94, 0.3);
    }}
    
    .input-container {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 25px;
        padding: 15px 20px;
        margin-top: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    
    .stTextInput > div > div > input {{
        background: transparent !important;
        border: none !important;
        color: white !important;
        font-size: 14px !important;
        padding: 0 !important;
        outline: none !important;
        box-shadow: none !important;
    }}
    
    .stTextInput > div > div > input::placeholder {{
        color: rgba(255, 255, 255, 0.6) !important;
    }}
    
    .stTextInput > div {{
        border: none !important;
        background: transparent !important;
    }}
    
    .stTextInput > label {{
        display: none !important;
    }}
    
    .send-button {{
        background: rgba(59, 130, 246, 0.9) !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 8px 20px !important;
        color: white !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(59, 130, 246, 0.3) !important;
        transition: all 0.2s ease !important;
    }}
    
    .send-button:hover {{
        background: rgba(59, 130, 246, 1) !important;
        transform: translateY(-1px) !important;
    }}
    
    .stButton > button {{
        background: rgba(59, 130, 246, 0.9) !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 8px 20px !important;
        color: white !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(59, 130, 246, 0.3) !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }}
    
    .stButton > button:hover {{
        background: rgba(59, 130, 246, 1) !important;
        transform: translateY(-1px) !important;
    }}
    
    .typing-indicator {{
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.8);
        padding: 12px 18px;
        border-radius: 20px;
        margin: 10px 0;
        max-width: 70%;
        margin-left: 0;
        margin-right: auto;
        font-size: 14px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
    }}
    
    .typing-dots {{
        display: inline-block;
    }}
    
    .typing-dots::after {{
        content: '';
        animation: typing 1.5s infinite;
    }}
    
    @keyframes typing {{
        0% {{ content: ''; }}
        25% {{ content: '.'; }}
        50% {{ content: '..'; }}
        75% {{ content: '...'; }}
        100% {{ content: ''; }}
    }}
    
    .fade-in {{
        animation: fadeIn 0.3s ease-in;
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>
    """, unsafe_allow_html=True)

def render_header():
    """Render the header with New Chat button"""
    st.markdown("""
    <div class="chat-header">
        <div class="new-chat-btn" onclick="window.location.reload()">New Chat</div>
        <div class="chat-title">START IMAGE SUMMARISING</div>
    </div>
    """, unsafe_allow_html=True)

def render_message(sender, message):
    """Render individual message bubble"""
    if sender == "System":
        st.markdown(f"""
        <div class="message-bubble system-message fade-in">
            {message}
        </div>
        """, unsafe_allow_html=True)
    elif sender == "You":
        st.markdown(f"""
        <div class="message-bubble fade-in">
            {message}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="message-bubble bot-message fade-in">
            {message}
        </div>
        """, unsafe_allow_html=True)

def render_typing_indicator():
    """Show typing indicator"""
    st.markdown("""
    <div class="typing-indicator">
        <span class="typing-dots">Start typing</span>
    </div>
    """, unsafe_allow_html=True)

def render_chat_messages(chat_history):
    """Render all chat messages"""
    st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
    
    for sender, message in chat_history:
        render_message(sender, message)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_input_area():
    """Render the input area"""
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            "",
            placeholder="Hi, I'm your AI agent please give me images to summarize.",
            key="user_input",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button("Send", key="send_btn", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return user_input, send_button

def initialize_session_state():
    """Initialize session state"""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [("System", "Hi, I'm your AI agent please give me images to summarize.")]