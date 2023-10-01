import streamlit as st

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

st.title("Scenario setup! ✍️")
st.markdown("## Set up your scenario here!")

# inputs
product = st.text_area('Product*', '', placeholder='Describe the product you want to sell')
customer_persona = st.text_area('Customer persona', '', placeholder='Want to practice selling to a specific customer persona? Describe them here! Leave blank if you want to practice selling to a generic customer.')
scenario = st.text_area('Scenario*', '', placeholder='Do you have a scenario in mind? A location, or niche details that you\'d like to test? Be as specific as possible!"')
level = st.selectbox('Level*', ('Easy', 'Medium', 'Hard'))

# describe levels
st.markdown("***Easy:*** Ideal for beginners or those new to the roles. The scenario will be straightforward with common challenges")
st.markdown("***Medium:*** Ideal for those with some experience in the roles. The scenario will be more complex with more difficult challenges")
st.markdown("***Hard:*** Ideal for those with a lot of experience in the roles. The scenario will be very complex with very difficult challenges")

# centered start button
col1, col2, col3 , col4, col5 = st.columns(5)
with col3 :
    center_button = st.button('Start!', type='primary')