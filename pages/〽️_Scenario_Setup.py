import streamlit as st
import time
from streamlit_extras.switch_page_button import switch_page
from Utils import hide_logout_login_pages

# this is the function that runs when the start button is clicked
def start_scenario():
    pass

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

# hide/unhide logout/login pages
hide_logout_login_pages("〽️_Scenario_Setup.py")

# redirect to login if needed
if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("You are not logged in! redirecting to login page...")
    # wait for a few seconds
    time.sleep(2)
    
    switch_page("login")

st.title("Scenario setup! ✍️")
st.markdown("## Set up your scenario here!")

with st.form("scenario_setup"):
    # inputs
    product = st.text_area('Product*', '', placeholder='Describe the product you want to sell')
    your_role = st.text_area('Your role', '', placeholder='Want to practice selling as a specific role? Describe it here! Leave blank if you want to practice selling as a customer service representative.')
    customer_persona = st.text_area('Customer persona', '', placeholder='Want to practice selling to a specific customer persona? Describe them here! Leave blank if you want to practice selling to a generic customer.')
    scenario = st.text_area('Scenario', '', placeholder='Do you have a scenario in mind? A location, or niche details that you\'d like to test? Be as specific as possible!"')
    level = st.selectbox('Level*', ('Easy', 'Medium', 'Hard'), index=1)

    # describe levels
    st.markdown("***Easy:*** Ideal for beginners or those new to the roles. The scenario will be straightforward with common challenges")
    st.markdown("***Medium:*** Ideal for those with some experience in the roles. The scenario will be more complex with more difficult challenges")
    st.markdown("***Hard:*** Ideal for those with a lot of experience in the roles. The scenario will be very complex with very difficult challenges")

    # centered start button
    col1, col2, col3 , col4, col5 = st.columns(5)
    with col3 :
        center_button = st.form_submit_button('Start!', on_click=start_scenario, type='primary', help='Click to start the scenario')
        
        # set some session state variables and redirect to scenario chat
        if center_button:
            # make sure required fields are filled
            if product == "" or level == "":
                st.error("Please fill in the required fields!")
                st.stop()

            st.session_state["scenario_has_been_setup"] = False
            st.session_state["scenario_product"] = product
            st.session_state["scenario_your_role"] = your_role
            st.session_state["scenario_customer_persona"] = customer_persona
            st.session_state["scenario_details"] = scenario
            st.session_state["scenario_level"] = level
            switch_page("scenario chat")
            