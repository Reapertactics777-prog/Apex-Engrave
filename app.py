import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

ROOT = Path(__file__).parent

# Browser tab icon: your JPG from the assets folder (falls back to an emoji if not found)
try:
    ICON = Image.open(ROOT / "assets" / "IMG-20261028-WA0027.jpg")
except Exception:
    ICON = "🪵"

st.set_page_config(
    page_title="Apex Engraving",
    page_icon=ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

IMAGES = {
    "LOGO": ("logo.png", "image/png"),
    "P1": ("p1.jpg", "image/jpeg"),
    "P2": ("p2.jpg", "image/jpeg"),
    "P3": ("p3.jpg", "image/jpeg"),
}


@st.cache_data
def build_html() -> str:
    """Load site.html and embed the images from the assets folder."""
    html = (ROOT / "site.html").read_text(encoding="utf-8")
    for token, (filename, mime) in IMAGES.items():
        raw = (ROOT / "assets" / filename).read_bytes()
        uri = f"data:{mime};base64,{base64.b64encode(raw).decode()}"
        html = html.replace(f"@@{token}@@", uri)
    return html


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

components.html(build_html(), height=900, scrolling=True)
