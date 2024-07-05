import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="MindBlower",
    page_icon=":alien:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Sidebar to input Google API Key
st.sidebar.title("Configuração Gemini Pro")
GOOGLE_API_KEY = st.sidebar.text_input("Insira sua chave API do Google AI Studio.", type="password")

# Guide for obtaining Google API Key if not available
st.sidebar.subheader("Não tem uma Chave API do Google?")
st.sidebar.write("Acesse o [Google AI Studio](https://aistudio.google.com/app/apikey) e faça login com sua conta do Google. Depois clique em Get API Key e coloque acima.")


# Check if API key is provided
if not GOOGLE_API_KEY:
    st.error("Insira sua chave API do Google AI Studio. ")
    st.stop()

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-1.5-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("MindBlower")

# Add small text below the header
st.markdown("Feito por 😎 [Guilherme](https://www.linkedin.com/in/guiborges7/)")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Pergunte ao ✨ Gemini-Pro...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
