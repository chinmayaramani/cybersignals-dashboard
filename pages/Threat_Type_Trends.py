import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Threat Type Trends", layout="wide")

BASE = Path(__file__).parents[1]
PH = BASE / "assets" / "placeholders"
VIS = BASE / "assets" / "visuals"

def get_img(name: str) -> Path:
    final = VIS / name
    return final if final.exists() else (PH / name)

st.title("Threat Type Trends")
st.caption("Summarizes which categories of cybercrime are rising and where attention should focus.")

st.image(str(get_img("threat_type_trends.png")), use_container_width=True)

st.subheader("What this answers")
st.write(
    "This view helps identify what kinds of attacks are most common (ransomware, fraud, supply chain, data theft) "
    "so recommendations can be tailored by sector."
)

st.subheader("Prototype insight")
st.write("Example: Ransomware remains a dominant pressure driver (illustrative).")

st.caption("Disclaimer: Prototype mockup using illustrative visuals. Final version will be backed by sourced incident datasets and reports.")
