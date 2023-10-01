import streamlit as st

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

st.title("Your Profile 🧑")
st.markdown("## Change your profile settings here!")

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