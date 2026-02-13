import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Incident Pressure", layout="wide")

BASE = Path(__file__).parents[1]
PH = BASE / "assets" / "placeholders"
VIS = BASE / "assets" / "visuals"

def get_img(name: str) -> Path:
    final = VIS / name
    return final if final.exists() else (PH / name)

st.title("Incident Pressure")
st.caption("Shows how cyber incidents are trending over time and which incident types are most common.")

st.image(str(get_img("incident_pressure.png")), use_container_width=True)

st.subheader("What this answers")
st.write(
    "This view helps answer: Are incidents increasing? Which incident types (e.g., ransomware, privacy breach, disruption) "
    "are driving the overall pressure?"
)

st.subheader("Prototype insight")
st.write("Example: Ransomware activity rises in later months (illustrative).")

st.caption("Disclaimer: Prototype mockup using illustrative visuals. Final version will be based on sourced incident data.")
