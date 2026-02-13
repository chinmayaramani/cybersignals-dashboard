import streamlit as st
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(page_title="Forecast Outlook", layout="wide")

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
st.title("🔮 Forecast Outlook")
st.caption(
    "Probability-based outlook of which sectors may face elevated cyber risk in the next 3–4 months."
)

# ----------------------------
# VISUAL
# ----------------------------
st.image(str(get_img("forecast_outlook.png")), use_container_width=True)

st.divider()

# ----------------------------
# INTERPRETATION
# ----------------------------
st.subheader("How to interpret this view")

st.markdown(
    """
    This outlook translates observed patterns — including seasonality, recent breach activity,
    and vulnerability signals — into a forward-looking risk perspective.

    The goal is not certainty, but early awareness to support:
    - Resource allocation  
    - Vendor risk tightening  
    - Security posture adjustments  
    - Executive planning discussions  
    """
)

# ----------------------------
# PROTOTYPE INSIGHT EXAMPLE
# ----------------------------
st.subheader("Illustrative Example")

st.write(
    "Example: Retail risk may increase approaching peak shopping periods due to elevated "
    "transaction volume and expanded attack surface."
)

# ----------------------------
# DISCLAIMER
# ----------------------------
st.warning(
    "Forecasting is probability-based and intended for awareness and planning — not deterministic prediction."
)

st.caption(
    "Prototype mockup using illustrative visuals. Final production version will document "
    "data sources, scoring methodology, and model assumptions."
)
