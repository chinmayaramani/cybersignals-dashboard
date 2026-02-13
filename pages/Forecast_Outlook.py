import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Forecast Outlook", layout="wide")

BASE = Path(__file__).parents[1]
PH = BASE / "assets" / "placeholders"
VIS = BASE / "assets" / "visuals"

def get_img(name: str) -> Path:
    final = VIS / name
    return final if final.exists() else (PH / name)

st.title("Forecast Outlook")
st.caption("Provides a probability-based outlook of which sectors may face higher risk in the next 3–4 months.")

st.image(str(get_img("forecast_outlook.png")), use_container_width=True)

st.subheader("How this is used")
st.write(
    "This supports planning by translating patterns (seasonality, exposure themes, and recent incident signals) into a forward-looking view."
)

st.warning("Prototype disclaimer: Forecasting is probability-based and intended for awareness and planning, not certainty.")

st.subheader("Prototype insight")
st.write("Example: Retail may rise approaching peak shopping periods (illustrative).")

st.caption("Disclaimer: Prototype mockup using illustrative visuals. Final version will document assumptions and scoring logic.")
