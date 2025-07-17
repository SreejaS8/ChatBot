# ui.py

import streamlit as st
import base64

def get_base64_image(image_path):
    """Convert image to base64 for CSS background"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def apply_custom_css():
    """Simple CSS with background image"""
    
    bg_image = get_base64_image("assets/background.jpg") or get_base64_image("assets/background.png")
    
    background_style = f"""
        background-image: url('data:image/jpeg;base64,{bg_image}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    """ if bg_image else """
        background: #1a1a2e;
    """
    
    st.markdown(f"""
    <style>
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
        background: rgba(0, 0, 0, 0.5);
        z-index: -1;
    }}
    
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{visibility: hidden;}}
    
    .chat-container {{
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }}
    
    .message {{
        background: rgba(255, 255, 255, 0.1);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    
    .user-message {{
        background: rgba(59, 130, 246, 0.8);
        margin-left: 20%;
    }}
    
    .bot-message {{
        background: rgba(255, 255, 255, 0.1);
        margin-right: 20%;
    }}
    
    .stTextInput > div > div > input {{
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 25px !important;
        color: white !important;
        padding: 10px 20px !important;
    }}
    
    .stTextInput > div > div > input::placeholder {{
        color: rgba(255, 255, 255, 0.6) !important;
    }}
    
    .stButton > button {{
        background: rgba(59, 130, 246, 0.8) !important;
        border: none !important;
        border-radius: 25px !important;
        color: white !important;
        padding: 10px 20px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

def render_message(sender, message):
    """Render a simple message"""
    if sender == "You":
        st.markdown(f'<div class="message user-message"><strong>You:</strong> {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message bot-message"><strong>Bot:</strong> {message}</div>', unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state"""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []