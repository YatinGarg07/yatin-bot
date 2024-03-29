import streamlit as st
from openai import OpenAI
import requests
import json
import random

st.set_page_config(
        page_title="Yatin's bot"                  
        )

st.title("Yatin's  Bot")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "audio_url" not in st.session_state:
    st.session_state["audio_url"] = ""

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])     

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
#All that's changed is that we've added a default model to st.session_state and set our OpenAI API key from Streamlit secrets. Here's where it gets interesting. We can replace our emulated stream with the model's responses from OpenAI:


    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
        thisList = ["Justin","Joanna","Kevin","Gregory","Matthew"]
        audioResponse = requests.post(
            st.secrets["LAMBDA_API_URL"],
            data = json.dumps({
                'text': ''.join(response),
                'voice': random.choice(thisList)
            }),
            timeout=10
            )
        audioJson = audioResponse.json()

        print(audioJson)
        if type(audioJson) != type(None):
            if type(audioJson['body']) != type(None):
                if type(audioJson['body']['url']) != type(None):
                    st.session_state["audio_url"] = audioJson["body"]['url'];

        # Function to load and display audio
        try:
            print("Audio Calling Displayed")
            st.audio( st.session_state["audio_url"] , format="audio/mp3" )
        except:
            print("Exception occurred")    
    
        #display_audio()

        
        #print(response)
    st.session_state.messages.append({"role": "assistant", "content": response})