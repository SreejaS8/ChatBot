import streamlit as st
import base64

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None

def apply_custom_css():
    bg_image = get_base64_image("./assets/background.jpg") or get_base64_image("./assets/background.png")

    # Use .webp for crisp modern background support too
    background_style = f"""
        background-image: url("data:image/jpeg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    """ if bg_image else """
        background: linear-gradient(120deg, #0f2027 0%, #2c5364 100%);
    """

    st.markdown(f"""
    <style>
    html, body, .stApp {{
        min-height: 100vh;
        {background_style}
        margin: 0;
        padding: 0;
        overflow-x: hidden;
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
    }}

    .stApp::before {{
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        background: rgba(0,0,0, 0.65);
        z-index: -2;
        pointer-events: none;
    }}

    .chat-container {{
        height: calc(100vh - 140px);
        overflow-y: auto;
        padding: 28px 0 36px 0;
        margin-bottom: 90px;
        scroll-behavior: smooth;
    }}

    .message {{
        padding: 16px 24px;
        margin: 20px 0 0 0;
        border-radius: 22px;
        animation: floatUp 0.5s cubic-bezier(0.22, 0.61, 0.36, 1) forwards;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.13);
        font-size: 17px;
        box-shadow: 0 6px 24px rgba(0,0,0,0.28);
        max-width: 80%;
        transition: background 0.25s, color 0.25s;
        line-height: 1.6;
        word-break: break-word;
        display: flex;
        flex-direction: column;
    }}

    .user-message {{
        align-items: flex-end;
        background: linear-gradient(135deg, rgba(41, 120, 255, 0.88) 0%, rgba(100,185,255,0.81) 100%);
        color: #fff;
        margin-left: auto;
        box-shadow: 0 8px 24px 2px rgba(30,118,210,0.09);
        border-bottom-right-radius: 6px;
    }}

    .bot-message {{
        align-items: flex-start;
        background: rgba(255,255,255,0.10);
        color: #fff;
        margin-right: auto;
        border-bottom-left-radius: 6px;
        box-shadow: 0 12px 30px 2px rgba(44,83,130,0.08);
    }}

    .sender {{
        font-weight: bold;
        font-size: 15px;
        margin-bottom: 3px;
        letter-spacing: 0.02em;
        opacity: 0.75;
    }}

    .stTextInput input {{
        background: rgba(255,255,255,0.11) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 12px 20px;
        border: 1.5px solid rgba(140,185,255,0.25);
        font-size: 16px;
        transition: border 0.2s;
        box-shadow: 0 2px 8px -1px rgba(44,153,255,0.08);
    }}

    .stTextInput input:focus {{
        border: 2px solid #299af4 !important;
        box-shadow: 0 2px 16px -3px rgba(44,153,255,0.15);
        outline: none !important;
    }}

    .stButton button {{
        background: linear-gradient(to right,#299af4, #6eb6fa);
        color: #fff;
        border: none;
        border-radius: 22px;
        padding: 10px 26px;
        font-weight: 600;
        margin-top: 8px;
        font-size: 16px;
        box-shadow: 0 2px 8px rgba(44,153,255,0.16);
        transition: background 0.2s;
    }}

    .stButton button:hover {{
        background: linear-gradient(90deg,#5acafe, #299af4);
    }}

    .input-bar {{
        position: fixed;
        bottom: 24px;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        max-width: 760px;
        padding: 0 14px;
        z-index: 12;
        background: rgba(15,32,39,0.92);
        border-radius: 16px;
        box-shadow: 0 5px 32px rgba(20,40,90,0.13);
    }}

    #MainMenu, footer, header, .stDeployButton {{
        visibility: hidden;
    }}

    @keyframes floatUp {{
        0% {{ transform: translateY(30px); opacity: 0; }}
        97% {{ opacity: 1; }}
        100% {{ transform: translateY(0); opacity: 1; }}
    }}
    </style>
    """, unsafe_allow_html=True)

def render_message(sender, message):
    """Enhanced message presentation: role above bubble, subtle color, emoji icon, word-wrap."""
    emoji = "🧑‍💻" if sender == "You" else "🤖"
    role_class = "user-message" if sender == "You" else "bot-message"
    st.markdown(
        f'''
        <div class="message {role_class}">
            <span class="sender">{emoji} {sender}</span>
            {message}
        </div>
        ''',
        unsafe_allow_html=True
    )
