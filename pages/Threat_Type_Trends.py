import streamlit as st
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(page_title="Threat Type Trends", layout="wide")

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
st.title("🧨 Threat Type Trends")
st.caption(
    "Trend analysis of dominant cybercrime categories impacting industrial sectors."
)

# ----------------------------
# VISUAL
# ----------------------------
st.image(str(get_img("threat_type_trends.png")), use_container_width=True)

st.divider()

# ----------------------------
# INTERPRETATION
# ----------------------------
st.subheader("How to interpret this view")

st.markdown(
    """
    This view highlights which attack categories are increasing in frequency or impact, such as:
    - Ransomware  
    - Data theft  
    - Fraud  
    - Supply chain compromise  
    - Operational disruption  

    Understanding attack type distribution allows sector-specific mitigation planning
    and targeted defensive investments.
    """
)

# ----------------------------
# ILLUSTRATIVE EXAMPLE
# ----------------------------
st.subheader("Illustrative Example")

st.write(
    "Example: Ransomware may remain a dominant pressure driver across multiple sectors, "
    "requiring strengthened backup, vendor, and endpoint protections."
)

# ----------------------------
# DISCLAIMER
# ----------------------------
st.warning(
    "This is a prototype visualization for layout and storytelling purposes. "
    "Final implementation will integrate validated, sourced incident datasets and industry reports."
)

st.caption(
    "Prototype mockup using illustrative visuals. Final production version will document "
    "data sources, categorization methodology, and update cadence."
)
