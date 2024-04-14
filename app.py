import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_input):
    return "I dont know"

#App config
st.set_page_config(page_title="ChatWeb",page_icon='🤖')
st.title("ChatWeB")

chat_history=[
    AIMessage(content="Hello, I am ChatWeb.How can i help you?"),
    
]

#Created the side bar
with st.sidebar:
    st.header("Settings")
    web_url=st.text_input("Website URL")

#Created the chat input
user_input=st.chat_input("Ask your questions...")
if user_input is not None and user_input!="":
    response=get_response(user_input)
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(HumanMessage(content=response))
    with st.chat_message("Human"):
        st.write(user_input)
    with st.chat_message("AI"):
        st.write(response)
    


