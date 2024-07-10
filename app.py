import streamlit as st
import pandas as pd

# Title
st.title("Goals-Based Wealth Management Prototype")

# Client Information Input
st.header("Client Information")
client_name = st.text_input("Client Name")
client_age = st.number_input("Client Age", min_value=18)
financial_goals = st.text_area("Financial Goals (e.g., Retirement, Education, Philanthropy)")

# Retirement Income Goal
st.header("Retirement Income Goal")
annual_retirement_income = st.number_input("Desired Annual Retirement Income ($)", min_value=0)
retirement_duration = st.number_input("Total Retirement Duration (years)", min_value=0)

# Define likelihood of success for different periods
first_period_years = 5
first_period_likelihood = 0.95
second_period_years = retirement_duration - first_period_years
second_period_likelihood = 0.75

# Calculate total goal amount for retirement income
first_period_amount = annual_retirement_income * first_period_years * first_period_likelihood
second_period_amount = annual_retirement_income * second_period_years * second_period_likelihood
total_retirement_goal = first_period_amount + second_period_amount

st.write(f"Total Retirement Goal Amount: ${total_retirement_goal:,.2f}")

# Detailed Goal Inputs
st.header("Other Goals")
num_goals = st.number_input("Number of Other Goals", min_value=0, max_value=10, step=1)

goals = [("Retirement Income", total_retirement_goal, retirement_duration)]
for i in range(num_goals):
    st.subheader(f"Goal {i+1}")
    goal_name = st.text_input(f"Goal {i+1} Name")
    goal_amount = st.number_input(f"Goal {i+1} Amount ($)", min_value=0)
    goal_horizon = st.number_input(f"Goal {i+1} Time Horizon (years)", min_value=0)
    goals.append((goal_name, goal_amount, goal_horizon))

current_assets = st.number_input("Current Assets ($)", min_value=0)
income = st.number_input("Annual Income ($)", min_value=0)
expenses = st.number_input("Annual Expenses ($)", min_value=0)

# Account Types Input
st.header("Account Types")
num_accounts = st.number_input("Number of Accounts", min_value=1, max_value=10, step=1)

accounts = []
for i in range(num_accounts):
    st.subheader(f"Account {i+1}")
    account_name = st.text_input(f"Account {i+1} Name")
    account_type = st.selectbox(f"Account {i+1} Type", ["Roth IRA", "IRA", "Taxable"])
    account_balance = st.number_input(f"Account {i+1} Balance ($)", min_value=0)
    accounts.append((account_name, account_type, account_balance))

# Portfolio Allocation
st.header("Portfolio Allocation")

def allocate_portfolio(goals):
    allocations = []
    for goal in goals:
        if "retirement income" in goal[0].lower():
            allocations.append({"Goal": goal[0], "Type": "Retirement", "Allocation": "Brunel's Retirement Allocation"})
        elif "short-term" in goal[0].lower():
            allocations.append({"Goal": goal[0], "Type": "Short-term Lifestyle", "Allocation": "Brunel's Short-term Allocation"})
        elif "long-term" in goal[0].lower():
            allocations.append({"Goal": goal[0], "Type": "Long-term Lifestyle", "Allocation": "Brunel's Long-term Allocation"})
        elif "purchasing power" in goal[0].lower():
            allocations.append({"Goal": goal[0], "Type": "Purchasing Power Protection", "Allocation": "Brunel's PP Allocation"})
        elif "growth" in goal[0].lower():
            allocations.append({"Goal": goal[0], "Type": "Growth", "Allocation": "Brunel's Growth Allocation"})
        else:
            allocations.append({"Goal": goal[0], "Type": "Uncategorized", "Allocation": "Brunel's Default Allocation"})
    return allocations

if st.button("Generate Portfolio"):
    allocations = allocate_portfolio(goals)
    st.subheader("Goal Allocations")
    for allocation in allocations:
        st.write(f"Goal: {allocation['Goal']}")
        st.write(f"Type: {allocation['Type']}")
        st.write(f"Allocation: {allocation['Allocation']}")
        st.write("---")

    st.success("Portfolio generated successfully!")

# Display Aggregated Portfolio
st.header("Aggregated Portfolio View")
st.write("This feature will display the aggregated portfolio across multiple accounts.")

# Generate Investment Policy Statement (IPS)
if st.button("Generate IPS"):
    ips = f"# Investment Policy Statement\n\n"
    ips += f"## Client Name: {client_name}\n"
    ips += f"## Client Age: {client_age}\n"
    ips += f"## Financial Goals: {financial_goals}\n\n"
    ips += f"## Account Types:\n"
    for account in accounts:
        ips += f"- {account[0]} ({account[1]}): ${account[2]}\n"
    ips += f"\n## Goal Allocations:\n"
    for allocation in allocations:
        ips += f"- Goal: {allocation['Goal']}, Type: {allocation['Type']}, Allocation: {allocation['Allocation']}\n"

    st.download_button(label="Download IPS", data=ips, file_name="investment_policy_statement.md", mime="text/markdown")
    st.success("Investment Policy Statement generated successfully!")

# Disclaimer
st.header("Disclaimer")
st.write("This software is for demonstration purposes only. It does not guarantee any results. Please consult with a financial advisor before making any investment decisions.")
