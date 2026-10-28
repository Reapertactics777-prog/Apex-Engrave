from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Apex Engraving",
    page_icon="🪵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's padding and chrome so the site fills the window.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden; height: 0;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stVerticalBlock"] {gap: 0;}
      iframe {height: 100vh !important; width: 100% !important; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_site() -> str:
    return (Path(__file__).parent / "site.html").read_text(encoding="utf-8")


components.html(load_site(), height=900, scrolling=True)
