import streamlit as st

def apply_custom_css():
    """
    Applies custom CSS for a clean and attractive UI.
    This includes the color theme, fonts, and fixed footer styling.
    """
    st.markdown("""
    <style>
    /* Hide Streamlit branding, footer, and header */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* Main app styling with a light, professional theme */
    .stApp {
        background: radial-gradient(ellipse at top, #F9E9D6 0%, #f0e1ca 40%, #e8d9be 100%);
        background-attachment: fixed;
        min-height: 100vh;
        padding-bottom: 80px; /* Space for the fixed footer */
        font-family: 'Arial', sans-serif;
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

    /* --- Title Styling --- */
    .app-title {
        text-align: center;
        color: #0700C5;
        font-size: 3rem;
        font-weight: 800;
        margin-top: 2rem;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 8px rgba(7, 0, 197, 0.15);
    }
    .app-subtitle {
        text-align: center;
        color: rgba(7, 0, 197, 0.7);
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 3rem;
    }

    /* --- Fixed Footer for Input --- */
    .fixed-bottom {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: rgba(249, 233, 214, 0.7);
        backdrop-filter: blur(15px);
        padding: 10px 20px;
        box-shadow: 0 -4px 12px rgba(7, 0, 197, 0.1);
        z-index: 1000;
    }

    /* --- Chat Messages Styling --- */
    .user-message {
        background: #0700C5;
        color: #F9E9D6;
        padding: 1rem 1.5rem;
        border-radius: 18px 18px 4px 18px;
        margin: 1rem 0;
        margin-left: 20%;
        box-shadow: 0 4px 12px rgba(7, 0, 197, 0.25);
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
        word-wrap: break-word;
        font-weight: 500;
        border: 1px solid rgba(7, 0, 197, 0.1);
    }

    /* --- Input and Button Styling --- */
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
    .stButton > button {
        background: #0700C5 !important;
        color: #F9E9D6 !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 15px 25px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(7, 0, 197, 0.3) !important;
        text-transform: uppercase !important;
    }

    </style>
    """, unsafe_allow_html=True)

def render_message(role, content):
    """Render a message with beautiful styling"""
    if role == "user":
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

def render_title_area():
    """Render the title and subtitle at the top of the page"""
    st.markdown('<h1 class="app-title">SuperLaw ⚖️</h1>', unsafe_allow_html=True)
    st.markdown('<p class="app-subtitle">Your Intelligent Legal Assistant</p>', unsafe_allow_html=True)
