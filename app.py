import streamlit as st
import requests

# Page setup and custom layout config
st.set_page_config(page_title="Mana Sonta ChatGPT", page_icon="🤖", layout="centered")

# Pure Clean UI Magic: Hiding all headers, icons, and text inside footer invisibly!
st.markdown("""
    <style>
    header, [data-testid="stHeader"], .stDeployButton, #MainMenu { visibility: hidden !important; display: none !important; }
    footer, div[data-testid="stFooter"], .viewerBadge_container__1QSob { visibility: hidden !important; display: none !important; }
    h1 a, .stMarkdown h1 a, div[data-testid="stDecoration"], div[data-testid="stToolbar"] { display: none !important; }
    [data-testid="stBottomBlockContainer"] footer { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Mana Sonta ChatGPT")
st.caption("Pure Unlimited High-Speed AI Chat Engine — Made for Short Films & Scripting")

# Initialize persistent memory state like ChatGPT
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat history layout smoothly
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Box (A to Z ChatGPT Structure)
if user_input := st.chat_input("Adagandi brother, ChatGPT laaga any topic automatic racha lepedham..."):
    # Show user prompt text instantly
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        try:
            # UNLIMITED CORE CHAT ENGINE (Bypassing all API Key limits permanently!)
            system_prompt = (
                "You are an advanced AI assistant built exactly like ChatGPT, named Mana Sonta ChatGPT. "
                "Always reply in friendly, casual Telugu using English script (Tanglish). "
                "You are an expert at everything from coding to writing short film scripts, action dialogue sequences, and ideas. "
                "Be incredibly polite, help the user with precise information, and use words like brother frequently."
            )
            
            # Formatting request packet securely
            url = f"https://text.pollinations.ai/{requests.utils.quote(user_input)}?system={requests.utils.quote(system_prompt)}"
            
            with st.spinner("Thinking like ChatGPT..."):
                res = requests.get(url, timeout=30)
                
            if res.status_code == 200:
                reply = res.text.strip()
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            else:
                st.error("Server loop loading error! Refresh chey anna.")
                    
        except Exception as e:
            st.error("Chinna technical data block clear kottu anna!")
