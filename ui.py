import streamlit as st

def apply_custom_css():
    """Apply custom CSS with clean fade-in animation"""
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

    /* Animated background */
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

    /* Success/Error messages */
    .stSuccess {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%) !important;
        border-radius: 15px !important;
    }

    .stError {
        background: linear-gradient(135deg, #ff6b6b 0%, #ffa8a8 100%) !important;
        border-radius: 15px !important;
    }

    /* Loading dots */
    .loading-dots {
        display: inline-block;
        position: relative;
        width: 80px;
        height: 80px;
    }

    .loading-dots div {
        position: absolute;
        top: 33px;
        width: 13px;
        height: 13px;
        border-radius: 50%;
        background: #0700C5;
        animation-timing-function: cubic-bezier(0, 1, 1, 0);
    }

    .loading-dots div:nth-child(1) {
        left: 8px;
        animation: loading1 0.6s infinite;
    }

    .loading-dots div:nth-child(2) {
        left: 8px;
        animation: loading2 0.6s infinite;
    }

    .loading-dots div:nth-child(3) {
        left: 32px;
        animation: loading2 0.6s infinite;
    }

    .loading-dots div:nth-child(4) {
        left: 56px;
        animation: loading3 0.6s infinite;
    }

    @keyframes loading1 {
        0% { transform: scale(0); }
        100% { transform: scale(1); }
    }

    @keyframes loading3 {
        0% { transform: scale(1); }
        100% { transform: scale(0); }
    }

    @keyframes loading2 {
        0% { transform: translate(0, 0); }
        100% { transform: translate(24px, 0); }
    }

    /* Hide main content initially for intro */
    .main .block-container {
        opacity: 0;
        transform: translateY(30px) scale(0.95);
        transition: all 1s ease-out;
    }

    /* Show content after intro */
    body.content-ready .main .block-container {
        opacity: 1;
        transform: translateY(0) scale(1);
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .stApp {
            padding: 1rem;
        }
        
        .user-message, .bot-message {
            margin-left: 5%;
            margin-right: 5%;
        }
        
        .chat-container {
            padding: 1rem;
            margin: 1rem auto;
        }
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

def render_startup_intro():
    """Render the dramatic zoom-in fade-out intro animation"""
    st.markdown("""
    <div class="intro-overlay" id="introOverlay">
        <div class="intro-title" id="introTitle">SuperLaw</div>
    </div>
    
    <script>
    function startIntroAnimation() {
        const overlay = document.getElementById('introOverlay');
        const title = document.getElementById('introTitle');
        
        if (!overlay || !title) return;
        
        // Phase 1: Title appears and grows (1.5 seconds)
        setTimeout(() => {
            title.classList.add('grow');
        }, 300);
        
        // Phase 2: Title zooms in dramatically and fades out (1 second)  
        setTimeout(() => {
            title.classList.add('zoom-fade');
        }, 1800);
        
        // Phase 3: Hide overlay and show content (0.5 seconds)
        setTimeout(() => {
            overlay.style.display = 'none';
            document.body.classList.add('content-ready');
        }, 2300);
    }
    
    // Start animation when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startIntroAnimation);
    } else {
        startIntroAnimation();
    }
    </script>
    
    <style>
    /* Intro overlay - full screen dramatic background */
    .intro-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(135deg, #F9E9D6 0%, #e6d5b8 50%, #d4c19a 100%);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        padding: 2rem;
    }
    
    /* Intro title - huge and dramatic */
    .intro-title {
        font-size: 15rem;
        font-weight: 800;
        color: #0700C5;
        text-align: center;
        letter-spacing: -8px;
        opacity: 0;
        transform: scale(0.3);
        transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        text-shadow: 0 8px 40px rgba(7, 0, 197, 0.3);
        line-height: 0.8;
    }
    
    /* Title grows to full huge size */
    .intro-title.grow {
        opacity: 1;
        transform: scale(1);
    }
    
    /* Title zooms in dramatically and fades out */
    .intro-title.zoom-fade {
        opacity: 0;
        transform: scale(4) translateY(-50px);
        transition: all 0.8s ease-in;
    }
    
    /* Mobile responsiveness for huge title */
    @media (max-width: 768px) {
        .intro-title {
            font-size: 8rem;
            letter-spacing: -4px;
        }
        
        .intro-title.zoom-fade {
            transform: scale(3) translateY(-30px);
        }
        
        .intro-overlay {
            padding: 1rem;
        }
    }
    
    @media (max-width: 480px) {
        .intro-title {
            font-size: 5rem;
            letter-spacing: -2px;
        }
        
        .intro-title.zoom-fade {
            transform: scale(2.5) translateY(-20px);
        }
    }
    </style>
    """, unsafe_allow_html=True)

def render_title_corner():
    """Render the subtitle after animation"""
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