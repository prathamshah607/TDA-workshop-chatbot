"""
TDA Chatbot - Simple & Clean
"""
import streamlit as st
from backend import ChatBackend
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="TDA Chatbot",
    layout="centered"
)

# Initialize session
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("Settings")
    
    api_key = st.text_input(
        "Groq API Key",
        value=os.getenv('GROQ_API_KEY', ''),
        type="password"
    )
    
    model = st.selectbox(
        "Model",
        ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
    )
    
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main
st.title("TDA Chatbot")

# Show messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("Type your message..."):
    if not api_key:
        st.error("Please add API key in sidebar")
        st.stop()
    
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Assistant response
    with st.chat_message("assistant"):
        backend = ChatBackend(api_key=api_key, model=model)
        messages = [{"role": "system", "content": "You are helpful."}]
        messages.extend(st.session_state.messages)
        response = st.write_stream(backend.stream_response(messages, temperature, 1024))
        st.session_state.messages.append({"role": "assistant", "content": response})
