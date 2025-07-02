import streamlit as st

def show_login():
    st.markdown("""
        <style>
        .login-box {
            background: #f0f2f6;
            padding: 2rem 2rem 1rem 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            max-width: 350px;
            margin: 3rem auto;
        }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.title("🔐 Login")
    username = st.text_input("Username or Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state["logged_in"] = True
        st.success("Login successful! Go to Transaction Form.")
    st.markdown('</div>', unsafe_allow_html=True) 