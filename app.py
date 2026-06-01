import streamlit as st
from google import genai
from google.genai import types

# Page setup and layout config
st.set_page_config(page_title="Mana Sonta AI Chatbot", page_icon="🤖", layout="centered")

# CSS Magic: Header elements, title links, buttons, watermarks ANNI completely VANISH!
st.markdown("""
    <style>
    /* Top Header and Deploy elements hide */
    header, [data-testid="stHeader"] {visibility: hidden !important; display: none !important;}
    .stDeployButton {display:none !important;}
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    
    /* Title pakkana unna extra anchor link or buttons hide cheyadaniki */
    h1 a {display: none !important;}
    .stMarkdown h1 a {display: none !important;}
    
    /* Decoration line and borders remove */
    div[data-testid="stDecoration"] { display: none !important; }
    .stCodeBlock { display: none !important; }
    div[data-testid="stToolbar"] { display: none !important; }
    button[title="View source"] { display: none !important; }
    
    /* Watermarks completely zero */
    .viewerBadge_container__1QSob { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Mana Sonta AI Chatbot")

API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Emaina adugu brother, racha lepedham..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    config = types.GenerateContentConfig(
        system_instruction="You are a helpful AI assistant. Always reply in friendly Telugu using English script (Tanglish). Be very polite, use words like brother, and keep the tone casual and cool.",
        temperature=0.7
    )
    
    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(model='gemini-2.5-flash', contents=user_input, config=config)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Problem!")
