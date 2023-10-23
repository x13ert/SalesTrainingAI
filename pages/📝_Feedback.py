import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
from Utils import hide_logout_login_pages
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
import hydralit_components as hc

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

# hide/unhide logout/login pages
hide_logout_login_pages("💬_Feedback.py")

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("You are not logged in! redirecting to login page...")
    # wait for a few seconds
    time.sleep(2)
    
    switch_page("login")

# if the history is not loaded, no scenario was (recently) started, redirect to feedback setup
if "chat_memory" not in st.session_state:
    st.warning("No scenario was started! redirecting to scenario page...")
    # wait for a few seconds
    time.sleep(2)
    switch_page("scenario setup")

# load the chat history and display it
chat_memory = st.session_state['chat_memory']
def populate_chat(chat_mem):

    # array to hold chat messages
    chat_messages = []

    # chat template
    for index, message in enumerate(chat_mem.messages):

        # skip the first message
        if index == 0:
            continue

        # also skip the message that asks for feedback, which is the last message
        if index == len(chat_mem.messages) - 1:
            continue

        if isinstance(message, HumanMessage):      
            # with ph:             
                human_msg = st.chat_message("human")
                human_msg.write(message.content)
                # add the message to the chat messages array
                chat_messages.append(human_msg)
        elif isinstance(message, AIMessage):
            # with ph: 
                ai_msg = st.chat_message("ai")
                ai_msg.write(message.content)
                chat_messages.append(ai_msg)

# create a chat completion that gives the user their score and feedback
def create_chat_completion(messages):
    from langchain.chat_models import ChatOpenAI
    chat = ChatOpenAI(model='gpt-4')
    new_message = chat.invoke(messages).content
    return new_message

# add a user message to the chat history, that asks the ai for feedback on the scenario and give a score

# create a copy of the chat memory
chat_memory = st.session_state['chat_memory']
chat_memory.add_user_message("*You will now give me feedback about my performance that includes what I did right, and what I could improve, and a score from 1 to 10 with 10 being the highest. Don't reply with any questions for me. Nothing else should be in response but the feedback, not even an indicator that this is your feedback*")

feedback_given = st.session_state['feedback_given']
if feedback_given == "":
    with st.spinner("Creating your personalized feedback..."):
        feedback_given = create_chat_completion(chat_memory.messages)
        st.session_state['feedback_given'] = feedback_given
st.title("Your personal feedback 📝:")
st.write(feedback_given)

# ask the user for feedback

# define what option labels and icons to display
option_data = [
    {'icon': "fa fa-question-circle", 'label':"No Feedback!"},
   {'icon': "bi bi-hand-thumbs-down", 'label':"Great Scenario!"},
   {'icon': "bi bi-hand-thumbs-up", 'label':"Average Scenario!"},
   {'icon':"bi bi-hand-thumbs-down",'label':"Bad Scenario!"},
]

# override the theme, else it will use the Streamlit applied theme
over_theme = {'txc_inactive': 'white','menu_background':'black','txc_active':'yellow','option_active':'blue'}
font_fmt = { 'font-size':'150%', 'font-class': 'h2'}

# display a horizontal version of the option bar
op = hc.option_bar(option_definition=option_data,title='Would you like to give feedback for this chat?',key='Opinion',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True, first_select=0)

# print the op
if op != "No Feedback!":
     st.success("Your feedback has been recorded!")

# populate the chat iwth the original chat history
populate_chat(st.session_state['chat_memory'])