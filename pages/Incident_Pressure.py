import streamlit as st
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(page_title="Incident Pressure", layout="wide")

# ----------------------------
# PATHS
# ----------------------------
BASE = Path(__file__).parents[1]
PH = BASE / "assets" / "placeholders"
VIS = BASE / "assets" / "visuals"

def get_img(name: str) -> Path:
    """Return final visual if available, else placeholder."""
    final = VIS / name
    return final if final.exists() else (PH / name)

# ----------------------------
# HEADER
# ----------------------------
st.title("📈 Incident Pressure")
st.caption(
    "Trend view of cyber incidents across sectors, highlighting intensity and dominant attack types."
)

# ----------------------------
# VISUAL
# ----------------------------
st.image(str(get_img("incident_pressure.png")), use_container_width=True)

st.divider()

# ----------------------------
# INTERPRETATION
# ----------------------------
st.subheader("How to interpret this view")

st.markdown(
    """
    This view highlights how incident volume and severity evolve over time.

    It helps decision-makers understand:
    - Whether incident frequency is increasing or stabilizing  
    - Which attack types are contributing most to disruption  
    - Where operational pressure may require response prioritization  
    """
)

# ----------------------------
# ILLUSTRATIVE EXAMPLE
# ----------------------------
st.subheader("Illustrative Example")

st.write(
    "Example: Ransomware-related incidents may show a seasonal increase "
    "in later months, contributing to elevated sector pressure."
)

# ----------------------------
# DISCLAIMER
# ----------------------------
st.warning(
    "This is a prototype visualization for layout and storytelling purposes. "
    "Final version will incorporate validated, sourced incident datasets."
)

st.caption(
    "Prototype mockup using illustrative visuals. Final implementation will document "
    "data sources and calculation methodology."
)
