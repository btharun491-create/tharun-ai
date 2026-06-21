import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="Mana Sonta AI", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF !important; color: #1a1a1a !important; }
    div[data-testid="stChatMessage"] { background-color: #f7f7f8 !important; border-radius: 8px; border: 1px solid #e5e5e7; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 Mana Sonta AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

# History display
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input logic
if user_input := st.chat_input("Ask anything..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        try:
            # Pollinations API URL structure
            encoded_user = requests.utils.quote(user_input)
            url = f"https://text.pollinations.ai/{encoded_user}?model=openai"
            
            with st.spinner("Thinking..."):
                res = requests.get(url, timeout=30)
                if res.status_code == 200:
                    reply = res.text
                    st.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                else:
                    st.error("Server busy, try again brother!")
        except Exception as e:
            st.error("Connection error vastondi brother, malli try cheyi!")
