import streamlit as st

# Title
st.title("Goals-Based Wealth Management Prototype")

# Client Information Input
st.header("Client Information")
client_name = st.text_input("Client Name")
client_age = st.number_input("Client Age", min_value=18)
risk_tolerance = st.selectbox("Risk Tolerance", ("Low", "Medium", "High"))
financial_goals = st.text_area("Financial Goals")
current_assets = st.number_input("Current Assets ($)", min_value=0)
income = st.number_input("Annual Income ($)", min_value=0)
expenses = st.number_input("Annual Expenses ($)", min_value=0)

# Portfolio Allocation
st.header("Portfolio Allocation")

def allocate_portfolio(risk_tolerance):
    if risk_tolerance == "Low":
        return {"Safety": 70, "Market": 20, "Aspirational": 10}
    elif risk_tolerance == "Medium":
        return {"Safety": 50, "Market": 30, "Aspirational": 20}
    else:
        return {"Safety": 30, "Market": 40, "Aspirational": 30}

if st.button("Generate Portfolio"):
    allocation = allocate_portfolio(risk_tolerance)
    st.subheader("Allocation")
    st.write(f"Safety Bucket: {allocation['Safety']}%")
    st.write(f"Market Bucket: {allocation['Market']}%")
    st.write(f"Aspirational Bucket: {allocation['Aspirational']}%")
    st.success("Portfolio generated successfully!")

# Display Aggregated Portfolio
st.header("Aggregated Portfolio View")
st.write("This feature will display the aggregated portfolio across multiple accounts.")
