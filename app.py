"""import streamlit as st

st.title("💰 Personal Expense Tracker")

st.write("Track your daily expenses")

import streamlit as st

st.title("💰 Personal Expense Tracker")

date = st.date_input("Date")

category = st.selectbox(
    "Category",
    ["Food", "Travel", "Shopping", "Bills", "Other"]
)

amount = st.number_input(
    "Amount",
    min_value=0.0
)

if st.button("Add Expense"):
    st.success("Expense Added Successfully!")"""
import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Personal Expense Tracker")

date = st.date_input("Date")

category = st.selectbox(
    "Category",
    ["Food", "Travel", "Shopping", "Bills", "Other"]
)

amount = st.number_input(
    "Amount",
    min_value=0.0
)

if st.button("Add Expense"):

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses(date, category, amount) VALUES (?, ?, ?)",
        (str(date), category, amount)
    )

    conn.commit()
    conn.close()

    st.success("Expense Saved Successfully!")

import pandas as pd

conn = sqlite3.connect("expenses.db")

df = pd.read_sql_query(
    "SELECT * FROM expenses",
    conn
)

st.subheader("Expense History")
st.dataframe(df)

conn.close()

