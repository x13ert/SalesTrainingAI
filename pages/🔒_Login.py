import time
import yaml
from yaml.loader import SafeLoader
import streamlit as st
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

if "authentication_status" in st.session_state and st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.write("You are logged in as: ", st.session_state["username"])
    #profile button
    if st.button("Profile", type='primary'):
        switch_page('profile')
else:
    st.title("Log-in! 🔒")
    st.markdown("## Welcome to BRIDGE 🌉. Fill in your information below to log-in!")

    # the login form
    with st.form("login_form"):
        # inputs
        username = st.text_input('Username*', '', placeholder='Enter your username')
        password = st.text_input('Password*', '', type='password', placeholder='Enter your password')

        # centered start button
        col1, col2, col3 , col4, col5 = st.columns(5)
        with col3 :
            login_button = st.form_submit_button('Login!', type='primary', help='Click to login')

        # set some session state variables and redirect to scenario chat
        if login_button:

            # make sure required fields are filled
            if username == "" or password == "":
                st.error("Please fill in the required fields!")
                st.stop()

            # try to login
            st_conn = st.connection('mysql', type='sql')
            try:
                df = st_conn.query(f"""SELECT * FROM Users WHERE username='{username}' AND password='{password}'""")

                # check if there is a row
                if len(df) == 0:
                    st.error("Username or password is incorrect!")
                    st.stop()

                # get the username, name and email
                username = df['username'][0]
                email = df['email'][0]
                user_id = df['id'][0]

                #save the session state variables
                st.session_state["authentication_status"] = True
                st.session_state["user_id"] = user_id
                st.session_state["username"] = username
                st.session_state["email"] = email


                # display success message and forward to scenario setup
                st.success("You logged in successfully! You will be redirected to the scenario setup page momentarily...")
                time.sleep(3)
                switch_page("scenario setup")
            except Exception as e:
                st.error(e)


    # create a not registered yet? signup button
    col1, col2, col3 , col4, col5 = st.columns(5,gap="small")
    with col4:
        st.write("Not registered yet?")
    with col5 :
        center_button = st.link_button('Signup!', type='primary', url='/Signup', use_container_width=True)
    
