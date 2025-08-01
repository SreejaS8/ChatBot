import streamlit as st

def apply_custom_css():
    """Apply stunning custom CSS to transform the Streamlit app"""
    st.markdown("""
    <style>
    /* Hide Streamlit branding and menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hide main content initially for startup animation */
    .main .block-container {
        opacity: 0;
        animation: mainContentFadeIn 0.8s ease-out 5s both;
    }
    
    @keyframes mainContentFadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #1a1a1a;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #f093fb, #f5576c);
    }

    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #1a1a2e 100%);
        background-attachment: fixed;
    }

    /* Animated background particles */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(120, 219, 255, 0.1) 0%, transparent 50%);
        animation: float 20s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-20px) rotate(1deg); }
        66% { transform: translateY(20px) rotate(-1deg); }
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

    /* Message bubbles */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 5px 20px;
        margin: 1rem 0;
        margin-left: 20%;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        animation: slideInRight 0.3s ease-out;
        position: relative;
        word-wrap: break-word;
    }

    .bot-message {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: #0a0a0a;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 20px 5px;
        margin: 1rem 0;
        margin-right: 20%;
        box-shadow: 0 4px 15px rgba(79, 172, 254, 0.3);
        animation: slideInLeft 0.3s ease-out;
        position: relative;
        word-wrap: break-word;
        font-weight: 500;
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
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 25px !important;
        color: white !important;
        padding: 15px 20px !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.4) !important;
        transform: translateY(-2px) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.6) !important;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 15px 30px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5) !important;
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
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
    """Render the startup intro animation"""
    st.markdown("""
    <div class="startup-overlay" id="startupOverlay">
        <div class="startup-title" id="startupTitle">
            SuperLaw
        </div>
    </div>
    
    <script>
    // Startup animation sequence
    function startupAnimation() {
        const overlay = document.getElementById('startupOverlay');
        const title = document.getElementById('startupTitle');
        
        if (!overlay || !title) return;
        
        // Phase 1: Title breathes in center (3 seconds)
        setTimeout(() => {
            title.classList.add('fly-to-corner');
        }, 3000);
        
        // Phase 2: Title flies to top-left (1.5 seconds)
        setTimeout(() => {
            overlay.classList.add('fade-out');
        }, 4500);
        
        // Phase 3: Hide overlay and show main content (0.5 seconds)
        setTimeout(() => {
            overlay.style.display = 'none';
            document.querySelector('.main-content').classList.add('breathe-in');
        }, 5000);
    }
    
    // Start animation when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startupAnimation);
    } else {
        startupAnimation();
    }
    </script>
    
    <style>
    /* Startup overlay - covers entire screen */
    .startup-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #1a1a2e 100%);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        transition: opacity 0.8s ease-out;
    }
    
    .startup-overlay.fade-out {
        opacity: 0;
        pointer-events: none;
    }
    
    /* Startup title - center screen, breathing */
    .startup-title {
        font-size: 6rem;
        font-weight: 900;
        background: linear-gradient(
            45deg,
            #667eea,
            #764ba2,
            #f093fb,
            #f5576c,
            #4facfe,
            #00f2fe,
            #667eea
        );
        background-size: 400% 400%;
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: 
            gradientShift 3s ease infinite,
            breatheIntro 2s ease-in-out infinite;
        text-shadow: 0 0 50px rgba(255, 255, 255, 0.3);
        letter-spacing: -3px;
        text-align: center;
        transition: all 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        transform-origin: center center;
    }
    
    /* Flying animation to top-left */
    .startup-title.fly-to-corner {
        position: fixed;
        top: 2rem;
        left: 2rem;
        font-size: 2.5rem;
        transform: scale(0.7);
        animation: none;
        z-index: 10000;
    }
    
    /* Breathing animation for intro */
    @keyframes breatheIntro {
        0%, 100% { 
            transform: scale(1) translateY(0px);
            filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.3));
        }
        50% { 
            transform: scale(1.08) translateY(-8px);
            filter: drop-shadow(0 0 40px rgba(102, 126, 234, 0.6));
        }
    }
    
    /* Main content breathing in */
    .main-content {
        opacity: 0;
        transform: translateY(30px) scale(0.95);
        transition: all 1s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .main-content.breathe-in {
        opacity: 1;
        transform: translateY(0) scale(1);
        animation: contentBreatheIn 0.8s ease-out;
    }
    
    @keyframes contentBreatheIn {
        0% {
            opacity: 0;
            transform: translateY(40px) scale(0.9);
        }
        60% {
            transform: translateY(-5px) scale(1.02);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }
    
    /* Hide main Streamlit content initially */
    .main .block-container {
        transition: all 0.5s ease-out;
    }
    
    /* Enhanced chat container breathing effect */
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
        transform: translateY(20px);
        opacity: 0;
        animation: chatBoxBreatheIn 1s ease-out 5.2s both;
    }
    
    @keyframes chatBoxBreatheIn {
        0% {
            opacity: 0;
            transform: translateY(40px) scale(0.95);
        }
        50% {
            transform: translateY(-5px) scale(1.02);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }
    
    /* Input bar breathing in */
    .input-bar {
        position: sticky;
        bottom: 0;
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(20px);
        padding: 1.5rem;
        border-radius: 20px 20px 0 0;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 2rem;
        transform: translateY(30px);
        opacity: 0;
        animation: inputBarBreatheIn 1s ease-out 5.5s both;
    }
    
    @keyframes inputBarBreatheIn {
        0% {
            opacity: 0;
            transform: translateY(50px);
        }
        70% {
            transform: translateY(-5px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Mobile responsiveness for startup */
    @media (max-width: 768px) {
        .startup-title {
            font-size: 3.5rem;
            letter-spacing: -1px;
        }
        
        .startup-title.fly-to-corner {
            font-size: 1.8rem;
            top: 1rem;
            left: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def render_title_corner():
    """Render the title in corner after animation"""
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <div style="text-align: center; color: rgba(255,255,255,0.7); font-size: 1.2rem;">
            Your Intelligent Legal Assistant
        </div>
    </div>
    """, unsafe_allow_html=True)