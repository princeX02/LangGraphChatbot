import streamlit as st
from langgraph1_backend import workflow
from langchain_core.messages import HumanMessage


config={'configurable':{ 'thread_id': '123'}}

# st.section_state -> 
if 'message_history' not in st.session_state:
        st.session_state['message_history'] = []
        


#Loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])
    



user_input =st.chat_input("Type your message here...")

if user_input:

    # first add the user message to the history
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    
  


    with st.chat_message("assistant"):
      
      ai_message=st.write_stream(
          message_chunk.content for message_chunk,metadata in  workflow.stream(
              {'messages': st.session_state['message_history']},
                config=config,
                stream_mode="messages"
          )
      )

    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})