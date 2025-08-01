import streamlit as st
import time

def apply_custom_css():
    """
    Applies custom CSS for a clean, animated chat interface.
    This includes a cream and blue color theme, animated backgrounds,
    and stylized message bubbles.
    """
    st.markdown("""
    <style>
    /* Hide Streamlit branding and menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main app styling with cream and blue theme */
    .stApp {
        background: radial-gradient(ellipse at top, #F9E9D6 0%, #f0e1ca 40%, #e8d9be 100%);
        background-attachment: fixed;
        min-height: 100vh;
        padding: 2rem;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
    }
    ::-webkit-scrollbar-track {
        background: rgba(249, 233, 214, 0.3);
        border-radius: 8px;
    }
    ::-webkit-scrollbar-thumb {
        background: #0700C5;
        border-radius: 8px;
    }

    /* Animated background bubbles */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image:
            radial-gradient(circle at 20% 50%, rgba(7, 0, 197, 0.05) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(249, 233, 214, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(7, 0, 197, 0.03) 0%, transparent 50%);
        animation: float 25s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-15px) rotate(0.5deg); }
        66% { transform: translateY(15px) rotate(-0.5deg); }
    }

    /* Message bubbles */
    .user-message {
        background: #0700C5;
        color: #F9E9D6;
        padding: 1rem 1.5rem;
        border-radius: 18px 18px 4px 18px;
        margin: 1rem 0;
        margin-left: 20%;
        box-shadow: 0 4px 12px rgba(7, 0, 197, 0.25);
        animation: slideInRight 0.4s ease-out;
        word-wrap: break-word;
    }

    .bot-message {
        background: #F9E9D6;
        color: #0700C5;
        padding: 1rem 1.5rem;
        border-radius: 18px 18px 18px 4px;
        margin: 1rem 0;
        margin-right: 20%;
        box-shadow: 0 4px 12px rgba(249, 233, 214, 0.4);
        animation: slideInLeft 0.4s ease-out;
        word-wrap: break-word;
        font-weight: 500;
        border: 1px solid rgba(7, 0, 197, 0.1);
    }

    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
    }

    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }

    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(249, 233, 214, 0.9) !important;
        backdrop-filter: blur(10px) !important;
        border: 2px solid rgba(7, 0, 197, 0.2) !important;
        border-radius: 20px !important;
        color: #0700C5 !important;
        padding: 15px 20px !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #0700C5 !important;
        box-shadow: 0 0 15px rgba(7, 0, 197, 0.3) !important;
        transform: translateY(-1px) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: rgba(7, 0, 197, 0.6) !important;
    }

    /* Button styling */
    .stButton > button {
        background: #0700C5 !important;
        color: #F9E9D6 !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 15px 25px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(7, 0, 197, 0.3) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 18px rgba(7, 0, 197, 0.4) !important;
        background: rgba(7, 0, 197, 0.9) !important;
    }

    /* Chat container */
    .chat-container {
        background: rgba(249, 233, 214, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(249, 233, 214, 0.15);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 800px;
        max-height: 500px;
        overflow-y: auto;
        box-shadow: 0 8px 24px rgba(7, 0, 197, 0.08);
    }
    
    /* Force main content to be visible by default */
    .main .block-container {
        opacity: 1;
        transform: none;
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .stApp { padding: 1rem; }
        .user-message, .bot-message { margin-left: 5%; margin-right: 5%; }
        .chat-container { padding: 1rem; margin: 1rem auto; }
    }
    </style>
    """, unsafe_allow_html=True)

def render_message(role, content):
    """Render a message with beautiful styling"""
    if role == "You":
        st.markdown(f"""
        <div class="user-message">
            <strong>You:</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="bot-message">
            <strong>SuperLaw AI:</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)

def render_title_corner():
    """Render the title and subtitle in the corner after animation"""
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0 3rem 0;">
        <h1 style="color: #0700C5; font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">
            SuperLaw
        </h1>
        <p style="color: rgba(7, 0, 197, 0.7); font-size: 1.2rem; font-weight: 500;">
            🏛️ Your Intelligent Legal Assistant
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_typing_indicator():
    """Show a typing indicator while AI is responding"""
    st.markdown("""
    <div class="bot-message">
        <strong>SuperLaw AI is thinking...</strong><br>
        <div class="loading-dots">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)