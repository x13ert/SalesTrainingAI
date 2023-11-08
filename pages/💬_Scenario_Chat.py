import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
from Utils import hide_logout_login_pages
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage

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

# load env variables with python-dotenv
from dotenv import load_dotenv
load_dotenv()

# this is the function that creates a chat completion using langchain
def create_chat_completion():
    from langchain.chat_models import ChatOpenAI
    chat = ChatOpenAI(model='gpt-4')
    messages = st.session_state['memory'].chat_memory.messages
    new_message = chat.invoke(messages).content
    st.session_state['memory'].chat_memory.add_ai_message(new_message)
    return new_message

def populate_chat():

    # array to hold chat messages
    chat_messages = []

    # chat template
    for index, message in enumerate(st.session_state['memory'].load_memory_variables({})['chat_history']):

        # skip the first message
        if index == 0:
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

    return chat_messages

def clear_chat(messages):
    for message in messages:
        del message

    

# if the scenario_has_been_setup session state variable doesn't exist, redirect to scenario setup
if "scenario_has_been_setup" not in st.session_state:
    switch_page("scenario setup")

# setup the scenario if it hasn't been setup yet
if not st.session_state["scenario_has_been_setup"]:
    # get the scenario details
    scenario_product = st.session_state["scenario_product"]
    scenario_customer_persona = st.session_state["scenario_customer_persona"]
    scenario_details = st.session_state["scenario_details"]
    scenario_level = st.session_state["scenario_level"]

    # if the role is not provided, set it to customer service representative
    if st.session_state["scenario_your_role"] == "":
         st.session_state["scenario_your_role"] = "Customer Service Representative"

    # setup the memory for the bot
    st.session_state['memory'] = ConversationBufferMemory(memory_key = "chat_history", input_key='question', output_key='answer', return_messages=True)
    st.session_state['memory'].chat_memory.add_ai_message(f"""This is a Sales / Customer Service Training Roleplay Prompt. You are playing the role of an excellent, friendly teacher and coach who helps teach via roleplay.

    During roleplay, I will play the role of the customer service representative (the learner). You will never play my role. I will never play as the customer. You will play the role of the customer and all other characters. The customer does not know who the learner is, such as their name, unless they specifically mention it. The amount of characters will be determined by the scenario - you can choose how many will be appropriate for learning purposes.

    Fields with a * are mandatory for the learner to provide details about, while any fields without * can be left blank, and you (ChatGPT) will fill them in for the user, with random but appropriate information. During the roleplay, try to maintain immersion by only replying to the characters you are controlling. Do not explain the rules of roleplay unless asked and let the roleplay proceed as though it was a regular conversation.

    --------
    0. Topic for Learning*: {scenario_product}
    1. Learner's Name*: {st.session_state["username"]}
    2. Learners Role*: {st.session_state["scenario_your_role"]}
    3. Customer Persona (Persona of the Main Roleplay Character): {scenario_customer_persona}
    4. Scenario: {scenario_details}
    5. Difficulty*: {scenario_level}
    - Easy: Ideal for beginners or those new to the role. The scenario will be straightforward with common challenges.
    - Medium: Suitable for those with some experience. The scenario will introduce more nuanced challenges and may involve multiple decision points.
    - Hard: Designer for professionals or those seeking a rigorous challenge. The scenario will be complex, with multiple layers of challenges, and unexpected twists, and may require advanced problem-solving skills.

    ----

    Create a challenging but fair scenario designed to teach them about the topic for learning. Always stay in-character as the customer and do not provide feedback until I ask for it. Your next message should describe the scenario to the learner, since the learner is playing the role of {st.session_state["scenario_your_role"]}, the scenario should be described in the third person and not to directly address the learner. At the end simulate the ringing of the phone, nothing else after that. The learner will then take over the role of the {st.session_state["scenario_your_role"]} and begin the roleplay. """)

    # create the first chat completion, display spinner while waiting
    with st.spinner("Generating scenario..."):
        create_chat_completion()

    # set the scenario has been setup session state variable
    st.session_state["scenario_has_been_setup"] = True

# display the scenario details
st.title("Scenario chat! 💬")
st.markdown("## Here is your scenario!")
st.markdown(f"***Product:*** {st.session_state['scenario_product']}")
st.markdown(f"***Your role:*** {st.session_state['scenario_your_role'] or 'Not provided'}")
st.markdown(f"***Customer persona:*** {st.session_state['scenario_customer_persona'] or 'Not provided'}")
st.markdown(f"***Scenario:*** {st.session_state['scenario_details'] or 'Not provided'}")
st.markdown(f"***Level:*** {st.session_state['scenario_level']}")

# chat placeholder
# ph = st.empty()

prompt = st.chat_input("Say something")
if prompt:
     # add message to history
    st.session_state['memory'].chat_memory.add_user_message(prompt)
    populate_chat()
    with st.spinner("Waiting for response..."):
        new_message = create_chat_completion()
        ai_msg = st.chat_message("ai")
        ai_msg.write(new_message)
else:
    populate_chat()

# something should show up here saying Finished? Click here to give feedback
if st.button("Finished? Click here to continue", type="primary"):
    # save the chat history to a session state variable
    st.session_state["chat_memory"] = st.session_state['memory'].chat_memory
    st.session_state["feedback_given"] = ""

    # switch to feedback page
    switch_page("feedback")


