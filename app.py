import streamlit as st
import requests

# Revert branding and set wide layout (PURE WHITE LIGHT THEME)
st.set_page_config(page_title="Mana Sonta AI", page_icon="🤖", layout="wide")

# Apply white theme logic for simple layout
st.markdown("""
    <style>
    /* Ensure default streamlit branding and headers are hidden for custom look */
    header, [data-testid="stHeader"], .stDeployButton, #MainMenu { visibility: hidden !important; display: none !important; }
    footer, div[data-testid="stFooter"], .viewerBadge_container__1QSob { visibility: hidden !important; display: none !important; }
    h1 a, .stMarkdown h1 a, div[data-testid="stDecoration"], div[data-testid="stToolbar"] { display: none !important; }
    [data-testid="stBottomBlockContainer"] footer { display: none !important; }
    
    /* Global White Theme Customization with Dark Text */
    .stApp { background-color: #FFFFFF !important; color: #1a1a1a !important; }
    div[data-testid="stChatMessage"] { background-color: #f7f7f8 !important; border-radius: 8px; margin-bottom: 10px; border: 1px solid #e5e5e7; color: #1a1a1a !important; }
    div[data-testid="stSidebar"] { background-color: #f0f0f2 !important; color: #1a1a1a !important; }
    
    /* Standard Input Box with dark text for contrast */
    .stChatInput textarea { color: #1a1a1a !important; }
    </style>
    """, unsafe_allow_html=True)

# Custom Sidebar logic with standard options
with st.sidebar:
    st.markdown("### 🤖 Mana Sonta AI")
    st.button("➕ New Chat", use_container_width=True)
    st.markdown("---")
    st.markdown("💬 *Recent History*")
    st.caption("• Creative Ideas")
    st.caption("• Action Dialogue Scene")
    st.caption("• Short Film Scripting")

# Apply the old title and wide-style layout logic
st.title("🤖 Mana Sonta AI")
st.caption("Pure Unlimited High-Speed AI Chat Engine — White Theme Layout")

# Initialize persistent memory state like ChatGPT
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat history layout smoothly
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Box (Active Chat Logic)
if user_input := st.chat_input("Ask anything..."):
    # Show user prompt text instantly
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        try:
            # DIRECT SECURE DATA STREAM STRING (100% SUCCESS RATE)
            system_rule = "You are Mana Sonta AI. Reply in friendly casual Telugu using English script (Tanglish). Be helpful and call the user brother frequently."
            
            # Clean formatting URL bypass
            encoded_user = requests.utils.quote(user_input)
            encoded_system = requests.utils.quote(system_rule)
            url = f"https://text.pollinations.ai/{encoded_user}?system={encoded_system}"
            
            with st.spinner("Thinking..."):
                res = requests.get(url, timeout=30)
                
            if res.status_code == 200 and res.text:
                reply = res.text.strip()
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            else:
                st.error("Server synchronization slow. Please press enter again brother!")
                    
        except Exception as e:
            st.error("Chinna technical connection clear kottu anna!")
