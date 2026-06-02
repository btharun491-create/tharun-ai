import streamlit as st

# Revert branding and set wide layout
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
