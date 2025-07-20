import streamlit as st
import base64

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def apply_custom_css():
    bg_image = get_base64_image("./assets/background.jpg") or get_base64_image("./assets/background.png")

    background_style = f"""
        background-image: url("data:image/jpeg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    """ if bg_image else """
        background: linear-gradient(to bottom right, #1a1a2e, #16213e);
    """

    st.markdown(f"""
    <style>
    html, body, .stApp {{
        height: 100%;
        {background_style}
        margin: 0;
        padding: 0;
        overflow: hidden;
    }}

    .stApp::before {{
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.55);
        z-index: -1;
    }}

    .chat-container {{
        height: calc(100vh - 100px);
        overflow-y: auto;
        padding: 20px;
        margin-bottom: 80px;
    }}

    .message {{
        padding: 16px;
        margin: 12px 0;
        border-radius: 15px;
        animation: floatUp 0.5s ease forwards;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        font-size: 16px;
        max-width: 75%;
    }}

    .user-message {{
        background: rgba(59, 130, 246, 0.75);
        color: #fff;
        margin-left: auto;
    }}

    .bot-message {{
        background: rgba(255, 255, 255, 0.1);
        color: #fff;
        margin-right: auto;
    }}

    .stTextInput input {{
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 25px;
        padding: 10px 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    .stButton button {{
        background: rgba(59, 130, 246, 0.9);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 24px;
        font-weight: bold;
    }}

    .input-bar {{
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        max-width: 800px;
        padding: 0 20px;
        z-index: 10;
        background: transparent;
    }}

    #MainMenu, footer, header, .stDeployButton {{
        visibility: hidden;
    }}

    @keyframes floatUp {{
        0% {{ transform: translateY(20px); opacity: 0; }}
        100% {{ transform: translateY(0); opacity: 1; }}
    }}
    </style>
    """, unsafe_allow_html=True)

def render_message(sender, message):
    if sender == "You":
        st.markdown(f'<div class="message user-message"><strong>{sender}:</strong> {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message bot-message"><strong>{sender}:</strong> {message}</div>', unsafe_allow_html=True)
