import streamlit as st
import requests

# Page setup for clean ChatGPT structure layout
st.set_page_config(page_title="Mana Sonta ChatGPT", page_icon="🤖", layout="wide")

# CSS Magic: Complete ChatGPT Mirror Look & Hiding Streamlit parameters completely
st.markdown("""
    <style>
    header, [data-testid="stHeader"], .stDeployButton, #MainMenu { visibility: hidden !important; display: none !important; }
    footer, div[data-testid="stFooter"], .viewerBadge_container__1QSob { visibility: hidden !important; display: none !important; }
    h1 a, .stMarkdown h1 a, div[data-testid="stDecoration"], div[data-testid="stToolbar"] { display: none !important; }
    [data-testid="stBottomBlockContainer"] footer { display: none !important; }
    
    /* Dark Theme Custom Accents */
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

# Initialize persistent memory state like ChatGPT
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
            # FIXED GLOBAL BACKUP ENGINE ROUTE (100% Crash Proof Validation)
            system_instruction = (
                "You are an advanced AI assistant built exactly like ChatGPT, named Mana Sonta ChatGPT. "
                "Always reply in friendly, casual Telugu using English script (Tanglish). "
                "You are a master at writing short film scripts, action dialogues, and everything else. "
                "Use words like brother frequently."
            )
            
            # Safe Request Payload Matrix Mapping
            payload = {
                "messages": [
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_input}
                ],
                "model": "openai",
                "json": False
            }
            
            with st.spinner("Thinking like ChatGPT..."):
                res = requests.post("https://text.pollinations.ai/", json=payload, timeout=30)
                
            if res.status_code == 200 and res.text:
                reply = res.text.strip()
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            else:
                # Dynamic Failover Fallback Method
                fallback_url = f"https://text.pollinations.ai/{requests.utils.quote(user_input)}"
                fallback_res = requests.get(fallback_url, timeout=30)
                if fallback_res.status_code == 200:
                    reply = fallback_res.text.strip()
                    st.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                else:
                    st.error("Server synchronization slow. Please press enter again brother!")
                    
        except Exception as e:
            st.error("Chinna technical sync loop clear kottu anna!")
