import streamlit as st

def apply_custom_css():
    """Apply stunning custom CSS to transform the Streamlit app"""
    st.markdown("""
    <style>
    /* Hide Streamlit branding and menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
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

def render_title():
    """Render the animated SuperLaw title"""
    st.markdown("""
    <div class="super-title">
        SuperLaw AI
    </div>
    <div style="text-align: center; color: rgba(255,255,255,0.7); font-size: 1.2rem; margin-bottom: 2rem;">
        Your Intelligent Legal Assistant
    </div>
    """, unsafe_allow_html=True)