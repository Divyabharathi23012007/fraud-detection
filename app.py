import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Fraud Detection App",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Transaction Form", "Result"])

if page == "Login":
    from pages.login import show_login
    show_login()
elif page == "Transaction Form":
    from pages.form import show_form
    show_form()
elif page == "Result":
    from pages.result import show_result
    show_result()
