import streamlit as st

def show_result():
    st.title("🔎 Prediction Result")
    prediction = st.session_state.get("prediction")
    if prediction is None:
        st.info("No prediction yet. Please submit a transaction.")
        return
    if prediction == 1:
        st.markdown("""
        <div style='background-color:#ffcccc;padding:2rem;border-radius:10px;text-align:center;'>
            <h2 style='color:#b30000;'>🚨 Fraudulent Transaction Detected!</h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background-color:#ccffcc;padding:2rem;border-radius:10px;text-align:center;'>
            <h2 style='color:#006600;'>✅ Legitimate Transaction</h2>
        </div>
        """, unsafe_allow_html=True) 