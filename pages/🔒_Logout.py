import yaml
from yaml.loader import SafeLoader
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from Utils import hide_logout_login_pages
import time


st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

# hide/unhide logout/login pages
hide_logout_login_pages("🔒_Logout.py")

# if logged out already, redirect to login page
if not "authentication_status" in st.session_state or not st.session_state["authentication_status"]:
    switch_page("login")

# tell user to click button to logout
st.title("Logout! 🔒")

st.write(f"Hey {st.session_state['username']}!")

st.write("Click the button below to logout!")

# button to logout
if st.button("Logout", type='primary'):

    # reset session state variables
    st.session_state["authentication_status"] = False
    del st.session_state["username"]
    del st.session_state["email"]
    del st.session_state["user_id"]

    # tell the user they logged out successfully
    st.success("You logged out successfully! Redirecting to login page momentarily...")

    # wait for a few seconds
    time.sleep(2)
    # show login again & redirect to login page
    hide_logout_login_pages("🔒_Logout.py")
    switch_page("login")




    
