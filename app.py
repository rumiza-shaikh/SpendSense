import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="SpendSense", layout="centered")
st.title("SpendSense: Real-Time Budgeting and Risk Visualization")

st.subheader("Enter Your Monthly Income and Fixed Expenses")
monthly_income = st.number_input("Monthly Income ($)", min_value=0, value=5000)
fixed_expenses = st.number_input("Fixed Monthly Expenses (e.g., rent, utilities) ($)", min_value=0, value=2000)

st.subheader("Log Your Discretionary Spending")
spending_data = []

for i in range(1, 6):
    with st.expander(f"Spending Entry {i}"):
        category = st.text_input(f"Category {i}", key=f"cat_{i}")
        amount = st.number_input(f"Amount Spent in {category}", min_value=0.0, key=f"amt_{i}")
        date = st.date_input(f"Date of Expense", value=datetime.date.today(), key=f"date_{i}")
        if category and amount:
            spending_data.append({"Category": category, "Amount": amount, "Date": date})

if st.button("Analyze Spending"):
    df = pd.DataFrame(spending_data)
    total_spent = df["Amount"].sum() if not df.empty else 0
    remaining_budget = monthly_income - fixed_expenses - total_spent

    st.write("Total Discretionary Spent: $", total_spent)
    st.write("Remaining Budget: $", remaining_budget)

    if remaining_budget < 0:
        st.error("You are over budget. Consider reducing discretionary spending.")
    elif remaining_budget < monthly_income * 0.1:
        st.warning("Your budget is tight. Monitor future expenses carefully.")
    else:
        st.success("You're managing your budget well.")

    st.dataframe(df)

st.markdown("---")
st.caption("Built with Streamlit")
