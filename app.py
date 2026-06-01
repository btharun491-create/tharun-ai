import streamlit as st
from google import genai
from google.genai import types

# Page setup and layout config
st.set_page_config(page_title="Mana Sonta AI Chatbot", page_icon="🤖", layout="centered")

# Ultra Clean Magic: Hiding all headers, icons, and text inside footer invisibly!
st.markdown("""
    <style>
    /* Hide top header, main menu and deploy buttons */
    header, [data-testid="stHeader"], .stDeployButton, #MainMenu { 
        visibility: hidden !important; 
        display: none !important; 
    }
    
    /* Remove title decoration lines and source buttons */
    h1 a, .stMarkdown h1 a, div[data-testid="stDecoration"], .stCodeBlock, div[data-testid="stToolbar"], button[title="View source"] { 
        display: none !important; 
    }
    
    /* TARGET FOOTER TEXT & LOGOS DIRECTLY WITHOUT BREAKING THE CHAT CONTAINER */
    footer, div[data-testid="stFooter"], .viewerBadge_container__1QSob {
        visibility: hidden !important;
    }
    
    /* Make the specific text span inside the status bar invisible */
    footer div, footer a, footer span, [data-testid="stBottomBlockContainer"] footer * {
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0px !important;
        font-size: 0px !important;
    }
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
