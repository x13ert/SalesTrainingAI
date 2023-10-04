import time
import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

st.title("Sign-up! ✍️")
st.markdown("### Welcome to BRIDGE 🌉")

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

try:
    if authenticator.register_user('Register user', preauthorization=False):
        with open('./streamlit-authenticator-config.yaml', 'w') as file:
            yaml.dump(auth_config, file, default_flow_style=False)
        st.success('You registered successfully! You will be redirected to the login page momentarily...')
        time.sleep(2)
        switch_page("login or logout")
except Exception as e:
    st.error(e)