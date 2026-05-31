import streamlit as str
from google import genai
from google.genai import types

str.set_page_config(page_title="Mana Sonta AI Chatbot", page_icon="😎", layout="centered")
str.title("😎 Mana Sonta AI Chatbot")
str.caption("🤖 Tharun AI — Local Style Chatbot")

# Pure Safe & Hidden Key
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
        system_instruction="You are a helpful AI assistant named Tharun AI. Always reply in friendly Telugu using English script (Tanglish). Be very polite, use words like 'brother', 'anne', and keep the tone casual and cool.",
        temperature=0.7
    )
    
    with str.chat_message("assistant"):
        with str.spinner("Wait chey brother, Tharun AI brain vaduthunna..."):
            try:
                response = client.models.generate_content(model='gemini-2.5-flash', contents=user_input, config=config)
                str.markdown(response.text)
                str.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                str.error("Problem!")
