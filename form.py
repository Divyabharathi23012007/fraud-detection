import streamlit as st
import xgboost as xgb
from pathlib import Path
import os
import numpy as np

def show_form():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if not st.session_state.get("logged_in"):
        st.warning("Please login first.")
        return
    st.title("💸 Transaction Input Form")
    st.markdown("Enter transaction details below:")
    with st.form("transaction_form"):
        amount = st.number_input("Transaction Amount", min_value=0.0, step=0.01)
        time = st.number_input("Transaction Time (seconds)", min_value=0)
        submitted = st.form_submit_button("Submit")
    if submitted:
        model_path = Path("fraud_detection_model.json")
        st.write("Current working directory:", os.getcwd())
        st.write("Files in directory:", os.listdir())
        if not model_path.exists():
            st.error("Model file not found. Please upload fraud_detection_model.json.")
            return
        try:
            model = xgb.XGBClassifier()
            model.load_model(str(model_path))
        except Exception as e:
            st.error(f"An error occurred while loading the model: {e}")
            return
        # Prepare input with 30 features: amount, time, and 28 dummy values (e.g., zeros)
        features = np.zeros((1, 30))
        features[0, 0] = amount
        features[0, 1] = time
        try:
            prediction = model.predict(features)[0]
            st.session_state["prediction"] = prediction
            st.success("Prediction complete! Go to Result page.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}") 