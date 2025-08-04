import streamlit as st
import time

# --- Page Config ---
st.set_page_config(
    page_title="SuperLaw - Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Elegant Law-Themed UI ---
st.markdown("""
    <style>
    body {
        background-color: #fdfcf7; /* soft parchment-like background */
        font-family: 'Segoe UI', sans-serif;
    }
    .chat-container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }
    .message {
        padding: 12px 16px;
        border-radius: 10px;
        margin-bottom: 12px;
        line-height: 1.5;
        font-size: 15px;
    }
    .user-message {
        background-color: DFD0B8; /* soft light blue */
        border: 1px solid #b3d1ff;
        align-self: flex-end;
    }
    .bot-message {
        background-color: 948979; /* light cream */
        border-left: 4px solid #c49a6c; /* gold accent */
    }
    .fixed-bottom {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #ffffff;
        padding: 12px 20px;
        border-top: 2px solid #c49a6c; /* gold line */
    }
    input, button {
        font-size: 16px !important;
    }
    .stButton>button {
        background-color: #c49a6c; /* gold */
        color: white;
        border: none;
        border-radius: 20px;
        padding: 8px 16px;
    }
    .stButton>button:hover {
        background-color: #a57f54; /* darker gold on hover */
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("SuperLaw - Your Legal Assistant")
st.write("Ask your legal questions and get responses like an advocate.")

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am SuperLaw, your legal assistant. How can I assist you today?"}
    ]

# --- Chat Display ---
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    role_class = "user-message" if msg["role"] == "user" else "bot-message"
    st.markdown(f'<div class="message {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Input ---
st.markdown('<div class="fixed-bottom">', unsafe_allow_html=True)
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input(
            "Ask a legal question...",
            placeholder="Type your legal question here...",
            key="user_input",
            label_visibility="collapsed"
        )
    with col2:
        submitted = st.form_submit_button("Send", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Handle Input ---
if submitted and user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Bot "advocate" style reply
    with st.spinner('SuperLaw is reviewing your case...'):
        time.sleep(1.5)
        response = (
            f"Based on the details you’ve provided, here is my preliminary legal opinion:\n\n"
            f"1. **Understanding Your Query:** {user_input}\n"
            "2. **Applicable Law:** This would depend on the jurisdiction and the specific facts of your case.\n"
            "3. **Suggested Next Steps:** Consider gathering all relevant documents and consulting with a licensed attorney for a formal review.\n\n"
            "Please note: This response is for informational purposes only and does not constitute legal advice."
        )
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
