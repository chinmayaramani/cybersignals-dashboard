import streamlit as st
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(page_title="Sector Risk Radar", layout="wide")

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
st.title("🧭 Sector Risk Radar")
st.caption(
    "Comparative view of cyber pressure across 10 major industrial sectors."
)

# ----------------------------
# VISUAL
# ----------------------------
st.image(str(get_img("sector_risk_radar.png")), use_container_width=True)

st.divider()

# ----------------------------
# INTERPRETATION
# ----------------------------
st.subheader("How to interpret this view")

st.markdown(
    """
    This radar ranks sectors based on relative cyber pressure, combining:
    - Incident frequency  
    - Exposure patterns  
    - Vulnerability signals  

    Higher scores suggest elevated risk exposure and may warrant closer monitoring,
    resource allocation, or defensive strengthening.
    """
)

# ----------------------------
# ILLUSTRATIVE EXAMPLE
# ----------------------------
st.subheader("Illustrative Example")

st.write(
    "Example: Healthcare and Retail may appear elevated relative to other sectors "
    "based on recent breach activity and exposure themes."
)

# ----------------------------
# DISCLAIMER
# ----------------------------
st.warning(
    "This is a prototype visualization for layout and storytelling purposes. "
    "Final implementation will incorporate validated data sources and documented scoring methodology."
)

st.caption(
    "Prototype mockup using illustrative visuals. Final production version will clearly document "
    "risk model assumptions and sector weighting logic."
)
