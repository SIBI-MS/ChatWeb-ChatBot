import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_input):
    return "I dont know"

#App config
st.set_page_config(page_title="ChatWeb",page_icon='🤖')
st.title("ChatWeB")

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[
    AIMessage(content="Hello, I am ChatWeb.How can i help you?"),
    
]
#Created the side bar
with st.sidebar:
    st.header("Settings")
    web_url=st.text_input("Website URL")

#Handling error when user trying to enter the url
if web_url is None or web_url=='':
    st.info("Please enter a valid URL")
else:
    #Created the chat input
    user_input=st.chat_input("Ask your questions...")
    if user_input is not None and user_input!="":
        response=get_response(user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        st.session_state.chat_history.append(AIMessage(content=response))
        # with st.chat_message("Human"):
        #     st.write(user_input)
        # with st.chat_message("AI"):
        #     st.write(response)
    # with st.sidebar:
    #     st.write(st.session_state.chat_history)
    
    
    #Chat conversations
    for message in st.session_state.chat_history:
        if isinstance(message,AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message,HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
        


        


