import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage #schemas
from langchain_community.document_loaders import WebBaseLoader  #load content from url
from langchain.text_splitter import RecursiveCharacterTextSplitter #used make chunks using the contents from url
from langchain_community.vectorstores import Chroma #to store vectors created my using the above chunks
from langchain.embeddings import FlagEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
#Storing apikey and model name
os.environ['HUGGINGFACE_API_KEY']=os.getenv("HUGGINGFACE_API_KEY")
model_id = 'tiiuae/falcon-7b-instruct'

#for get response to the user
def get_response(user_input):
    return "I dont know"

#storing the contents from the url
def get_vector_store_from_url(url):
    loader=WebBaseLoader(url)
    
    #store contents from url
    documents=loader.load()
    
    #creating chunks
    documents=get_chunks(documents)
    
    #storing vectors in chroma
    vector_store=Chroma.from_documents(documents_chunks,FlagEmbeddings())
    
    return vector_store

#creating chunks using the website contents
def get_chunks(documents):
    text_splitter=RecursiveCharacterTextSplitter()
    documents_chunks=text_splitter.split_documents(documents)
    return documents_chunks




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
    documents_chunks=get_vector_store_from_url(web_url)
    # with st.sidebar:
    #     st.write(documents_chunks)
    
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
        


        


