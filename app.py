import streamlit as st
from google import genai

# Page setup
st.set_page_config(page_title="Mana Sonta AI")
st.title("🤖 Mana Sonta AI")

# API key ni Streamlit Secrets lo set cheyi (Settings -> Secrets)
api_key = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat history display
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Em adagali anukuntunnav?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Gemini Model call
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt
            )
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error vachindi: {e}")
