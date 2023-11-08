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
# with open('./streamlit-authenticator-config.yaml') as file:
#     auth_config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     auth_config['credentials'],
#     auth_config['cookie']['name'],
#     auth_config['cookie']['key'],
#     auth_config['cookie']['expiry_days'],
#     auth_config['preauthorized']
# )

# try:
#     if authenticator.register_user('Register user', preauthorization=False):
#         with open('./streamlit-authenticator-config.yaml', 'w') as file:
#             yaml.dump(auth_config, file, default_flow_style=False)
#         st.success('You registered successfully! You will be redirected to the login page momentarily...')
#         time.sleep(1.5)
#         switch_page("login")
# except Exception as e:
#     st.error(e)

# the registration form
with st.form("registration_form"):
    # inputs
    username = st.text_input('Username*', '', placeholder='Enter your username')
    password = st.text_input('Password*', '', type='password', placeholder='Enter your password')
    password_confirm = st.text_input('Confirm password*', '', type='password', placeholder='Confirm your password')
    name = st.text_input('Name*', '', placeholder='Enter your name')
    email = st.text_input('Email*', '', placeholder='Enter your email')

    # centered start button
    col1, col2, col3 , col4, col5 = st.columns(5)
    with col3 :
        register_button = st.form_submit_button('Register!', type='primary', help='Click to register')

    # set some session state variables and redirect to scenario chat
    if register_button:
        from sqlalchemy import text

        # make sure required fields are filled
        if username == "" or password == "" or password_confirm == "" or name == "" or email == "":
            st.error("Please fill in the required fields!")
            st.stop()

        # make sure passwords match
        if password != password_confirm:
            st.error("Passwords do not match!")
            st.stop()

        # register account
        st_conn = st.connection('mysql', type='sql')
        connection = st_conn.connect()
        try:
            trans = connection.begin()
            result = connection.execute(text(f"""INSERT INTO Users (username, email, password) VALUES ('{username}','{email}','{password}')"""))
            trans.commit()
            st.success("You registered successfully! You will be redirected to the login page momentarily...")
            time.sleep(3)
            switch_page("login")
        except:
            st.error("Something went wrong! This username or email may already be taken! Please try again!")
            st.stop()
        # check the result
        # if result:
        #     st.success("You registered successfully! You will be redirected to the login page momentarily...")
        #     time.sleep(1.5)
        #     switch_page("login")
        # else:
        #     st.error("Something went wrong! Please try again!")
        #     st.stop()

# connect to mysql
# conn = st.connection('mysql', type='sql')

# display the streamlit dataframe
# st.write(df)


# this is the registration widget


