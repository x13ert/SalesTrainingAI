import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
from Utils import hide_logout_login_pages

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

# hide/unhide logout/login pages
hide_logout_login_pages("💬_Scenario_Chat.py")

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("You are not logged in! redirecting to login page...")
    # wait for a few seconds
    time.sleep(2)
    
    switch_page("login")


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

# chat template
with st.chat_message("assistant"):
    st.markdown("***Prospect:*** I'm interested in some new widgets!")

with st.chat_message("user"):
    st.markdown("***You:*** Great! I'd be happy to help you with that. What kind of widgets are you looking for?")

prompt = st.chat_input("Say something")