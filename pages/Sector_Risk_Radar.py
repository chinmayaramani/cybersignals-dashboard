import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Sector Risk Radar", layout="wide")

BASE = Path(__file__).parents[1]
PH = BASE / "assets" / "placeholders"
VIS = BASE / "assets" / "visuals"

def get_img(name: str) -> Path:
    final = VIS / name
    return final if final.exists() else (PH / name)

st.title("Sector Risk Radar")
st.caption("Ranks the 10 sectors by current cyber pressure to highlight where attention is most needed.")

st.image(str(get_img("sector_radar.png")), use_container_width=True)

st.subheader("How to read this")
st.write(
    "Higher scores indicate greater cyber pressure based on observed incident frequency and sector exposure. "
    "This view helps leadership prioritize attention and allocate resources."
)

st.subheader("Prototype insight")
st.write("Example: Healthcare and Retail appear elevated compared to other sectors (illustrative).")

st.caption("Disclaimer: Prototype mockup using illustrative visuals. Final dashboard will use validated sources and documented scoring logic.")
