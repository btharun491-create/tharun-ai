import streamlit as st
import requests

# Page setup for clean layout
st.set_page_config(page_title="Mana Sonta ChatGPT", page_icon="🤖", layout="wide")

# CSS Magic: Complete ChatGPT Mirror Look (Dark/Light sidebar adjustments & hide watermarks)
st.markdown("""
    <style>
    /* Hide default Streamlit headers, menus and footers */
    header, [data-testid="stHeader"], .stDeployButton, #MainMenu { visibility: hidden !important; display: none !important; }
    footer, div[data-testid="stFooter"], .viewerBadge_container__1QSob { visibility: hidden !important; display: none !important; }
    h1 a, .stMarkdown h1 a, div[data-testid="stDecoration"], div[data-testid="stToolbar"] { display: none !important; }
    [data-testid="stBottomBlockContainer"] footer { display: none !important; }
    
    /* Custom Styling to mimic ChatGPT Structure */
    .stApp { background-color: #212121; color: #ececec; }
    div[data-testid="stChatMessage"] { background-color: #2f2f2f; border-radius: 8px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ChatGPT Sidebar Mirror Layout Simulation
with st.sidebar:
    st.markdown("### 🤖 Mana ChatGPT")
    st.button("➕ New Chat", use_container_width=True)
    st.markdown("---")
    st.markdown("💬 *Recent History*")
    st.caption("• Short Film Scripting")
    st.caption("• Action Dialogue Scene")
    st.caption("• Creative Ideas")

st.title("🤖 Mana Sonta ChatGPT")
st.caption("Pure Unlimited High-Speed AI Chat Engine — Built exactly like ChatGPT Layout")

# Initialize persistent memory state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat history layout smoothly
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Box (A to Z ChatGPT Core Structure)
if user_input := st.chat_input("Ask anything..."):
    # Show user prompt text instantly
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        try:
            # PURE UNLIMITED CHAT ENGINE (No API Key Required, Zero Loop Errors)
            url = f"https://text.pollinations.ai/{requests.utils.quote(user_input)}"
            params = {
                "system": "You are an advanced AI assistant built exactly like ChatGPT, named Mana Sonta ChatGPT. Always reply in friendly, casual Telugu using English script (Tanglish). You are a master at everything: writing short film scripts, action dialogues, and everything else. Use words like brother frequently.",
                "model": "searchgpt",
                "private": "true"
            }
            
            with st.spinner("Thinking like ChatGPT..."):
                res = requests.get(url, params=params, timeout=30)
                
            if res.status_code == 200:
                reply = res.text.strip()
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            else:
                st.error("Connection refresh trigger needed brother! Enter malli kottu anna.")
                    
        except Exception as e:
            st.error("Chinna data streaming bypass kottu anna!")
