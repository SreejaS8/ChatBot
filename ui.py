import streamlit as st

def apply_custom_css():
    """Apply stunning custom CSS to transform the Streamlit app"""
    st.markdown("""
    <style>
    /* Hide Streamlit branding and menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hide main Streamlit content initially for startup animation */
    .main .block-container {
        opacity: 0;
        animation: mainContentFadeIn 0.8s ease-out 4s both;
    }
    
    @keyframes mainContentFadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Main app styling with cream and blue theme */
    .stApp {
        background: radial-gradient(ellipse at top, #F9E9D6 0%, #f0e1ca 40%, #e8d9be 100%);
        background-attachment: fixed;
        min-height: 100vh;
    }
    
    /* Custom scrollbar with blue theme */
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
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(7, 0, 197, 0.8);
    }

    /* Animated background with cream tones */
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

    /* SuperLaw Title Animation */
    .super-title {
        font-size: 4rem;
        font-weight: 800;
        text-align: center;
        margin: 2rem 0;
        background: linear-gradient(
            45deg,
            #667eea,
            #764ba2,
            #f093fb,
            #f5576c,
            #4facfe,
            #00f2fe
        );
        background-size: 400% 400%;
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 3s ease infinite, breathe 4s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.5);
        letter-spacing: -2px;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes breathe {
        0%, 100% { transform: scale(1) translateY(0px); }
        50% { transform: scale(1.05) translateY(-5px); }
    }

    /* Chat container */
    .chat-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        max-height: 500px;
        overflow-y: auto;
        position: relative;
    }

    /* Message bubbles with blue and cream theme */
    .user-message {
        background: #0700C5;
        color: #F9E9D6;
        padding: 1rem 1.5rem;
        border-radius: 18px 18px 4px 18px;
        margin: 1rem 0;
        margin-left: 20%;
        box-shadow: 0 4px 12px rgba(7, 0, 197, 0.25);
        animation: slideInRight 0.4s ease-out;
        position: relative;
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
        position: relative;
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

    /* Input styling with blue and cream theme */
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

    /* Button styling with blue theme */
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

    /* Form container */
    .input-bar {
        position: sticky;
        bottom: 0;
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(20px);
        padding: 1.5rem;
        border-radius: 20px 20px 0 0;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 2rem;
    }

    /* Loading animation */
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
        background: #667eea;
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

    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(0, 0, 0, 0.8) !important;
        backdrop-filter: blur(20px) !important;
    }

    /* Success/Error messages */
    .stSuccess {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%) !important;
        border-radius: 15px !important;
        animation: fadeInScale 0.5s ease-out !important;
    }

    .stError {
        background: linear-gradient(135deg, #ff6b6b 0%, #ffa8a8 100%) !important;
        border-radius: 15px !important;
        animation: shake 0.5s ease-out !important;
    }

    @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }

    @keyframes shake {
        0%, 20%, 40%, 60%, 80% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .super-title {
            font-size: 2.5rem;
        }
        
        .user-message, .bot-message {
            margin-left: 5%;
            margin-right: 5%;
            border-radius: 15px;
        }
        
        .chat-container {
            padding: 1rem;
            margin: 1rem 0;
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
    """Render the Netflix-style startup intro animation"""
    st.markdown("""
    <div class="netflix-intro-overlay" id="netflixIntro">
        <div class="netflix-title" id="netflixTitle">
            SuperLaw
        </div>
        <div class="netflix-flash" id="netflixFlash"></div>
    </div>
    
    <script>
    // Netflix-style startup animation sequence
    function netflixStartupAnimation() {
        const overlay = document.getElementById('netflixIntro');
        const title = document.getElementById('netflixTitle');
        const flash = document.getElementById('netflixFlash');
        
        if (!overlay || !title || !flash) return;
        
        // Phase 1: Title appears and grows (1.5 seconds)
        setTimeout(() => {
            title.classList.add('appear');
        }, 200);
        
        // Phase 2: Dramatic zoom and flash (1 second)
        setTimeout(() => {
            title.classList.add('zoom-dramatic');
            flash.classList.add('flash-effect');
        }, 1700);
        
        // Phase 3: Complete fade out and show content (0.8 seconds)
        setTimeout(() => {
            overlay.classList.add('complete-fadeout');
        }, 2500);
        
        // Phase 4: Remove overlay and show main content
        setTimeout(() => {
            overlay.style.display = 'none';
        }, 3300);
    }
    
    // Start Netflix animation when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', netflixStartupAnimation);
    } else {
        netflixStartupAnimation();
    }
    </script>
    
    <style>
    /* Netflix-style startup overlay - covers entire screen */
    .netflix-intro-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: #000000;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        overflow: hidden;
    }
    
    .netflix-intro-overlay.complete-fadeout {
        opacity: 0;
        transition: opacity 0.8s ease-out;
        pointer-events: none;
    }
    
    /* Netflix-style title - starts invisible */
    .netflix-title {
        font-size: 8rem;
        font-weight: 900;
        color: #0700C5;
        text-align: center;
        letter-spacing: -3px;
        opacity: 0;
        transform: scale(0.3) translateY(50px);
        text-shadow: 
            0 0 20px rgba(7, 0, 197, 0.3),
            0 0 40px rgba(7, 0, 197, 0.2),
            0 0 80px rgba(7, 0, 197, 0.1);
        position: relative;
        z-index: 10001;
        font-family: 'Arial Black', sans-serif;
    }
    
    /* Title appears with smooth entrance */
    .netflix-title.appear {
        opacity: 1;
        transform: scale(1) translateY(0);
        transition: all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        animation: pulseGlow 2s ease-in-out;
    }
    
    /* Dramatic zoom effect like Netflix */
    .netflix-title.zoom-dramatic {
        transform: scale(15) translateZ(0);
        opacity: 0;
        transition: all 0.8s cubic-bezier(0.25, 0.1, 0.25, 1);
        filter: blur(2px);
    }
    
    /* Pulsing glow effect */
    @keyframes pulseGlow {
        0%, 100% {
            text-shadow: 
                0 0 20px rgba(7, 0, 197, 0.3),
                0 0 40px rgba(7, 0, 197, 0.2),
                0 0 80px rgba(7, 0, 197, 0.1);
        }
        50% {
            text-shadow: 
                0 0 30px rgba(7, 0, 197, 0.6),
                0 0 60px rgba(7, 0, 197, 0.4),
                0 0 120px rgba(7, 0, 197, 0.2);
        }
    }
    
    /* Flash effect like Netflix logo flash */
    .netflix-flash {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(
            circle at center,
            rgba(255, 255, 255, 0.9) 0%,
            rgba(7, 0, 197, 0.3) 30%,
            transparent 70%
        );
        opacity: 0;
        z-index: 10000;
        pointer-events: none;
    }
    
    .netflix-flash.flash-effect {
        opacity: 1;
        animation: netflixFlash 0.6s ease-out;
    }
    
    @keyframes netflixFlash {
        0% {
            opacity: 0;
            transform: scale(0.5);
        }
        30% {
            opacity: 1;
            transform: scale(1.2);
        }
        70% {
            opacity: 0.8;
            transform: scale(2);
        }
        100% {
            opacity: 0;
            transform: scale(4);
        }
    }
    
    /* Enhanced chat container that appears after Netflix intro */
    .chat-container {
        background: rgba(249, 233, 214, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(249, 233, 214, 0.15);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 
            0 8px 24px rgba(7, 0, 197, 0.08),
            inset 0 1px 0 rgba(249, 233, 214, 0.1);
        max-height: 500px;
        overflow-y: auto;
        position: relative;
        transform: translateY(15px);
        opacity: 0;
        animation: chatBoxSlideIn 0.8s ease-out 4.2s both;
    }
    
    @keyframes chatBoxSlideIn {
        0% {
            opacity: 0;
            transform: translateY(25px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Input bar appears after Netflix intro */
    .input-bar {
        position: sticky;
        bottom: 0;
        background: rgba(7, 0, 197, 0.85);
        backdrop-filter: blur(15px);
        padding: 1.5rem;
        border-radius: 16px 16px 0 0;
        border-top: 1px solid rgba(249, 233, 214, 0.2);
        margin-top: 2rem;
        transform: translateY(20px);
        opacity: 0;
        animation: inputBarSlideIn 0.8s ease-out 4.5s both;
    }
    
    @keyframes inputBarSlideIn {
        0% {
            opacity: 0;
            transform: translateY(30px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Mobile responsiveness for Netflix intro */
    @media (max-width: 768px) {
        .netflix-title {
            font-size: 4rem;
            letter-spacing: -2px;
        }
        
        .netflix-title.zoom-dramatic {
            transform: scale(8) translateZ(0);
        }
    }
    
    /* Additional Netflix-style touches */
    .netflix-intro-overlay::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 30% 40%, rgba(7, 0, 197, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 70% 60%, rgba(7, 0, 197, 0.05) 0%, transparent 50%);
        z-index: 9998;
    }
    </style>
    """, unsafe_allow_html=True)

def render_title_corner():
    """Render the title in corner after animation"""
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <div style="text-align: center; color: rgba(7, 0, 197, 0.8); font-size: 1.5rem; font-weight: 600;">
            🏛️ Your Intelligent Legal Assistant
        </div>
    </div>
    """, unsafe_allow_html=True)