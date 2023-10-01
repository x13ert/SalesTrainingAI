import streamlit as st

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

# chat template
with st.chat_message("assistant"):
    st.markdown("***Prospect:*** I'm interested in some new widgets!")

with st.chat_message("user"):
    st.markdown("***You:*** Great! I'd be happy to help you with that. What kind of widgets are you looking for?")

prompt = st.chat_input("Say something")