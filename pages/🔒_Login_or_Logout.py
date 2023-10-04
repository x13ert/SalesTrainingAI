import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

# load authenticator
with open('./streamlit-authenticator-config.yaml') as file:
    auth_config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    auth_config['credentials'],
    auth_config['cookie']['name'],
    auth_config['cookie']['key'],
    auth_config['cookie']['expiry_days'],
    auth_config['preauthorized']
)


if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.write("You are logged in as: ", st.session_state["username"])
    #profile button
    if st.button("Profile", type='primary'):
        switch_page('profile')
    authenticator.logout('Logout', 'main', key='unique_key')
else:
    st.title("Log-in! 🔒")
    st.markdown("## Welcome to BRIDGE 🌉. Fill in your information below to log-in!")
    try:
        authenticator.login('Login', 'main')
    except Exception as e:
        st.error(e)

    if st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    if st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    
