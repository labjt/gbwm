import streamlit as st

# Title
st.title("Goals-Based Wealth Management Prototype")

# Client Information Input
st.header("Client Information")
client_name = st.text_input("Client Name")
client_age = st.number_input("Client Age", min_value=18)
risk_tolerance = st.selectbox("Overall Risk Tolerance", ("Low", "Medium", "High"))
financial_goals = st.text_area("Financial Goals (e.g., Retirement, Education, Philanthropy)")

# Detailed Goal Inputs
st.header("Detailed Goals")
num_goals = st.number_input("Number of Goals", min_value=1, max_value=10, step=1)

goals = []
for i in range(num_goals):
    st.subheader(f"Goal {i+1}")
    goal_name = st.text_input(f"Goal {i+1} Name")
    goal_amount = st.number_input(f"Goal {i+1} Amount ($)", min_value=0)
    goal_horizon = st.number_input(f"Goal {i+1} Time Horizon (years)", min_value=0)
    goal_risk_tolerance = st.selectbox(f"Goal {i+1} Risk Tolerance", ("Low", "Medium", "High"))
    goals.append((goal_name, goal_amount, goal_horizon, goal_risk_tolerance))

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

def detailed_allocation(goal_risk_tolerance):
    if goal_risk_tolerance == "Low":
        return {"Safety": 80, "Market": 15, "Aspirational": 5}
    elif goal_risk_tolerance == "Medium":
        return {"Safety": 60, "Market": 30, "Aspirational": 10}
    else:
        return {"Safety": 40, "Market": 40, "Aspirational": 20}

if st.button("Generate Portfolio"):
    overall_allocation = allocate_portfolio(risk_tolerance)
    st.subheader("Overall Allocation")
    st.write(f"Safety Bucket: {overall_allocation['Safety']}%")
    st.write(f"Market Bucket: {overall_allocation['Market']}%")
    st.write(f"Aspirational Bucket: {overall_allocation['Aspirational']}%")

    for i, (goal_name, goal_amount, goal_horizon, goal_risk_tolerance) in enumerate(goals):
        goal_allocation = detailed_allocation(goal_risk_tolerance)
        st.subheader(f"Allocation for {goal_name}")
        st.write(f"Safety Bucket: {goal_allocation['Safety']}%")
        st.write(f"Market Bucket: {goal_allocation['Market']}%")
        st.write(f"Aspirational Bucket: {goal_allocation['Aspirational']}%")
    
    st.success("Portfolio generated successfully!")

# Display Aggregated Portfolio
st.header("Aggregated Portfolio View")
st.write("This feature will display the aggregated portfolio across multiple accounts.")
