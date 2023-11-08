import streamlit as st
import time
from streamlit_extras.switch_page_button import switch_page
from Utils import hide_logout_login_pages

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

# hide/unhide logout/login pages
hide_logout_login_pages("🧑_Profile.py")

# redirect to login if needed
if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("You are not logged in! redirecting to login page...")
    # wait for a few seconds
    time.sleep(2)
    
    switch_page("login")

st.title("Your Profile 🧑")
st.markdown("## Change your profile settings here!")
st.markdown("( This feature is currently unavailable )")

st.stop()

# inputs
username = st.text_input('Your username (this is how the AI will address you)*', '')
jobtitle = st.text_input('Your job title*', '')
yearsofsalesexperience = st.text_input('Your years of sales experience*', '')
company = st.text_input('Your company (optional)', '')
location = st.text_input('Your location (optional)', '')

# centered save button
col1, col2, col3 , col4, col5 = st.columns(5)
with col3 :
    center_button = st.button('Save', type='primary')