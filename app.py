import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CyberSignals", layout="wide")

BASE = Path(__file__).parent
PH = BASE / "assets" / "placeholders"
VIS = BASE / "assets" / "visuals"

def get_img(name: str) -> Path:
    """Use final visual if it exists, otherwise fallback to placeholder."""
    final = VIS / name
    return final if final.exists() else (PH / name)

st.title("CyberSignals")
st.caption("Prototype mock dashboard (layout + storytelling).")

st.markdown(
    "CyberSignals is a sector-level cyber risk radar designed to help business and IT audiences "
    "understand **which sectors are under pressure**, **what is driving risk**, and **what actions to take**."
)

# Sidebar (prototype filters)
st.sidebar.header("Filters (Prototype)")
st.sidebar.multiselect(
    "Sector",
    ["Communications","Energy","Financials","Healthcare","Industrials","Materials","Real Estate","Retail","Technology","Utilities"],
    default=["Energy","Healthcare","Retail"]
)
st.sidebar.selectbox("Time Range", ["Last 30 days", "Last Quarter", "Last 12 months"])
st.sidebar.selectbox("Threat Type", ["All", "Ransomware", "Data Theft", "Fraud", "Supply Chain", "Operational Disruption"])
st.sidebar.info("Note: Filters are placeholders for the mockup. Later they will drive real charts.")

cards = [
    ("Sector Risk Radar", "Which industries look most exposed right now?", "sector_radar.png"),
    ("Incident Pressure", "Are incidents increasing? What’s driving the pressure?", "incident_pressure.png"),
    ("Vulnerability Signals", "What weaknesses are being exploited most?", "vuln_signals.png"),
    ("Forecast Outlook", "Which sectors may be at higher risk next (probability-based)?", "forecast_outlook.png"),
]

st.subheader("Dashboard Overview")

col1, col2 = st.columns(2, gap="large")
for i, (title, desc, img_name) in enumerate(cards):
    target = col1 if i % 2 == 0 else col2
    with target:
        st.markdown(f"### {title}")
        st.caption(desc)
        st.image(str(get_img(img_name)), use_container_width=True)

st.markdown("### Threat Type Trends")
st.caption("What types of cybercrime are trending?")
st.image(str(get_img("threat_type_trends.png")), use_container_width=True)

st.divider()
st.caption("Disclaimer: Prototype mockup using illustrative visuals for layout/storytelling. Final version will use validated sources and documented methodology.")
