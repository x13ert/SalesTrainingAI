import streamlit as st

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

st.title("Log-in! 🔒")
st.markdown("## This is a placeholder")

# inputs
username = st.text_input('Username*', '')
pwd = st.text_input('Password*', '')

# centered sign-up button
col1, col2, col3 , col4, col5 = st.columns(5)
with col3 :
    center_button = st.button('Log-in!', type='primary')

