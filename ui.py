# ui.py

import streamlit as st
from datetime import datetime

def apply_custom_css():
    """Apply custom CSS styling to the Streamlit app"""
    st.markdown("""
    <style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container styling */
    .main-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 20px;
    }
    
    /* Chat container */
    .chat-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* Title styling */
    .chat-title {
        text-align: center;
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .chat-subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    
    /* Message styling */
    .message {
        margin: 15px 0;
        padding: 15px;
        border-radius: 15px;
        animation: fadeIn 0.5s ease-in;
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: 20%;
        text-align: right;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .bot-message {
        background: rgba(255, 255, 255, 0.9);
        color: #333;
        margin-right: 20%;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .system-message {
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        font-style: italic;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Message sender labels */
    .message-sender {
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 5px;
        opacity: 0.8;
    }
    
    /* Input area styling */
    .input-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 30px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 16px;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.3);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.5);
    }
    
    /* Status indicator */
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        background: #4CAF50;
        border-radius: 50%;
        margin-right: 10px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    /* Loading animation */
    .loading-dots {
        display: inline-block;
    }
    
    .loading-dots:after {
        content: '...';
        animation: dots 1.5s steps(4, end) infinite;
    }
    
    @keyframes dots {
        0%, 20% { color: rgba(0,0,0,0); text-shadow: .25em 0 0 rgba(0,0,0,0), .5em 0 0 rgba(0,0,0,0); }
        40% { color: #333; text-shadow: .25em 0 0 rgba(0,0,0,0), .5em 0 0 rgba(0,0,0,0); }
        60% { text-shadow: .25em 0 0 #333, .5em 0 0 rgba(0,0,0,0); }
        80%, 100% { text-shadow: .25em 0 0 #333, .5em 0 0 #333; }
    }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    """Render the app header"""
    st.markdown("""
    <div class="chat-title">
        🤖 Groq Chat Assistant
    </div>
    <div class="chat-subtitle">
        <span class="status-indicator"></span>
        Powered by LLaMA3 & Groq API
    </div>
    """, unsafe_allow_html=True)

def render_message(sender, message, message_type="normal"):
    """Render a chat message with proper styling"""
    timestamp = datetime.now().strftime("%H:%M")
    
    if message_type == "system":
        st.markdown(f"""
        <div class="message system-message">
            <div class="message-sender">System • {timestamp}</div>
            {message}
        </div>
        """, unsafe_allow_html=True)
    elif sender == "You":
        st.markdown(f"""
        <div class="message user-message">
            <div class="message-sender">You • {timestamp}</div>
            {message}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="message bot-message">
            <div class="message-sender">🤖 Assistant • {timestamp}</div>
            {message}
        </div>
        """, unsafe_allow_html=True)

def render_input_area():
    """Render the input area with custom styling"""
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            "Message", 
            placeholder="Type your message here...",
            key="user_input",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button("Send", key="send_btn", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return user_input, send_button

def render_chat_history(chat_history):
    """Render the chat history with proper styling"""
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    for i, (sender, message) in enumerate(chat_history):
        if sender == "System":
            render_message(sender, message, "system")
        else:
            render_message(sender, message)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_typing_indicator():
    """Show typing indicator while processing"""
    st.markdown("""
    <div class="message bot-message">
        <div class="message-sender">🤖 Assistant</div>
        <div class="loading-dots">Thinking</div>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Render sidebar with additional options"""
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.chat_history = [("System", "Hi! I'm your Groq-powered chatbot. Say something!")]
            st.rerun()
        
        st.markdown("---")
        
        # Model info
        st.markdown("### 🧠 Model Info")
        st.info("**Model:** LLaMA3-8B-8192\n**Provider:** Groq\n**Max Tokens:** 8192")
        
        st.markdown("---")
        
        # Tips
        st.markdown("### 💡 Tips")
        st.markdown("""
        - Ask questions naturally
        - Request explanations or examples
        - Try creative writing prompts
        - Ask for code help
        - Get summaries of topics
        """)
        
        st.markdown("---")
        
        # Stats
        if "chat_history" in st.session_state:
            total_messages = len(st.session_state.chat_history) - 1  # Exclude system message
            st.markdown(f"### 📊 Session Stats")
            st.metric("Messages", total_messages)

def show_error_message(error_text):
    """Display error message with custom styling"""
    st.markdown(f"""
    <div class="message bot-message" style="border-left: 4px solid #ff6b6b; background: rgba(255, 107, 107, 0.1);">
        <div class="message-sender">❌ Error</div>
        {error_text}
    </div>
    """, unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [("System", "Hi! I'm your Groq-powered chatbot. Say something!")]
    
    if "processing" not in st.session_state:
        st.session_state.processing = False