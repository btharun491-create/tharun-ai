import streamlit as st

# Page setup and custom layout config
st.set_page_config(page_title="Mana AI Image Creator", page_icon="🎨", layout="centered")

# Pure Clean UI Magic: Hiding all headers, icons, and text inside footer invisibly!
st.markdown("""
    <style>
    header, [data-testid="stHeader"], .stDeployButton, #MainMenu { visibility: hidden !important; display: none !important; }
    footer, div[data-testid="stFooter"], .viewerBadge_container__1QSob { visibility: hidden !important; display: none !important; }
    h1 a, .stMarkdown h1 a, div[data-testid="stDecoration"], div[data-testid="stToolbar"] { display: none !important; }
    [data-testid="stBottomBlockContainer"] footer { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 Mana AI Image Creator")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat history layout smoothly
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Box
if user_input := st.chat_input("Emaina prompt type chey brother, image generate cheddham..."):
    # Show user prompt text instantly
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        try:
            # NO API PASS KEY REQUIRED: Formatting direct keyword input stream safely
            clean_prompt = user_input.replace(" ", "-").lower()
            image_url = f"https://image.pollinations.ai/p/{clean_prompt}?width=1024&height=1024&nologo=true"
            
            st.markdown("Sure brother! Idhigo nuvvu adigina image ready: 🔥")
            
            # Using clean direct markdown image rendering to prevent broken symbol zeros
            st.markdown(f"![Generated Image]({image_url})")
            
            # Save layout logic state
            st.session_state.messages.append({
                "role": "assistant", 
                "content": f"Sure brother! Idhigo nuvvu adigina image ready: 🔥\n\n![Generated Image]({image_url})"
            })
                
        except Exception as e:
            st.error("Chinna technical block clear kottu anna!")
