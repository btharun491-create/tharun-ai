import streamlit as str
from google import genai
from google.genai import types

# Page setup and layout config
str.set_page_config(page_title="Mana Sonta AI Chatbot", page_icon="🤖", layout="centered")

# CSS Magic: Crown, Deploy, Menu, GitHub Link & borders ANNI completely HIDE avthayi!
str.markdown("""
    <style>
    header {visibility: hidden !important;}
    .stDeployButton {display:none !important;}
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    div[data-testid="stDecoration"] { display: none !important; }
    div[data-testid="stHeader"] { display: none !important; }
    .stCodeBlock { display: none !important; }
    
    /* GitHub repository link and viewer options completely hide cheyadaniki */
    div[data-testid="stToolbar"] { display: none !important; }
    button[title="View source"] { display: none !important; }
    .viewerBadge_container__1QSob { display: none !important; }
    </style>
    """, unsafe_content_allowed=True)

str.title("🤖 Mana Sonta AI Chatbot")

API_KEY = str.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)

if "messages" not in str.session_state:
    str.session_state.messages = []

for message in str.session_state.messages:
    with str.chat_message(message["role"]):
        str.markdown(message["content"])

if user_input := str.chat_input("Emaina adugu brother, racha lepedham..."):
    with str.chat_message("user"):
        str.markdown(user_input)
    str.session_state.messages.append({"role": "user", "content": user_input})
    
    config = types.GenerateContentConfig(
        system_instruction="You are a helpful AI assistant. Always reply in friendly Telugu using English script (Tanglish). Be very polite, use words like brother, and keep the tone casual and cool.",
        temperature=0.7
    )
    
    with str.chat_message("assistant"):
        try:
            response = client.models.generate_content(model='gemini-2.5-flash', contents=user_input, config=config)
            str.markdown(response.text)
            str.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            str.error("Problem!")
