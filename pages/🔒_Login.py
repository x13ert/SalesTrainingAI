import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from Utils import hide_logout_login_pages

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

# if logged in, redirect to scenario setup
if "authentication_status" in st.session_state and st.session_state["authentication_status"]:
    switch_page("scenario setup")

# hide/unhide logout/login pages
hide_logout_login_pages("🔒_Login.py")

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

        # create a not registered yet? signup button
        col1, col2, col3 , col4, col5 = st.columns(5,gap="small")
        with col4:
            st.write("Not registered yet?")
        with col5 :
            center_button = st.link_button('Signup!', type='primary', url='/Signup', use_container_width=True)
    except Exception as e:
        st.error(e)

    if st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    if st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    
