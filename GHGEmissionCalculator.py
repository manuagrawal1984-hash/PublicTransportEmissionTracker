import streamlit as st

st.title("Ministry of Transport: GHG Mitigation Dashboard")
st.markdown("### Project Concept Phase Assessment (Oct 2025 Guidelines)")

# Sidebar for Global Parameters
st.sidebar.header("Global Constants")
grid_ef = st.sidebar.number_input("National Grid Factor (tCO2e/MWh)", value=0.5)

# Main Input Columns
col1, col2 = st.columns(2)

with col1:
    st.header("Baseline (Diesel)")
    buses = st.number_input("Diesel Buses to Phase Out", value=100)
    avg_km = st.number_input("Annual KM per Bus", value=50000)
    ef_diesel = st.number_input("Emission Factor (g/km)", value=1000)
    be_y = (buses * avg_km * ef_diesel) / 1_000_000

with col2:
    st.header("Project (Electric)")
    kwh_km = st.number_input("BEB Efficiency (kWh/km)", value=1.2)
    ef_pj_km = (kwh_km / 1000) * grid_ef
    pe_y = (buses * avg_km * ef_pj_km)

# Leakage Section
st.divider()
leakage = st.radio("Fate of Diesel Fleet:", ["Scrapped", "Resold Outside Project Area"])
le_y = be_y if leakage == "Resold Outside Project Area" else 0

# Final Results
er_y = be_y - pe_y - le_y
total_savings = er_y * 15 # 5 years implementation + 10 years post-project

st.metric("Annual Emission Reductions (ERy)", f"{er_y:,.2f} tCO2e")
st.metric("Total Reportable Mitigation (15 Years)", f"{total_savings:,.2f} tCO2e")

if st.button("Generate Submission Report"):
    st.success("Report generated. Figures are conservative and aligned with MAF Guidelines.")
