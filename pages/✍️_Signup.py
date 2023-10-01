import streamlit as st

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

st.title("Sign-up! ✍️")
st.markdown("## This is a placeholder")

# inputs
email = st.text_input('Your e-mail*', '')
username = st.text_input('Username*', '')
pwd = st.text_input('Password*', '', type='password')

# centered sign-up button
col1, col2, col3 , col4, col5 = st.columns(5)
with col3 :
    center_button = st.button('Sign-up!', type='primary')

