import streamlit as st

st.set_page_config(page_title="ChatWeb",page_icon='🤖')
st.title("ChatWeB")

#Created the side bar
with st.sidebar:
    st.header("Settings")
    web_url=st.text_input("Website URL")

#Created the chat input
st.chat_input("Ask your questions...")

#Dummy chats
with st.chat_message("AI"):
    st.write("How can i help you?")
with st.chat_message("Human"):
    st.write("Nothing")
