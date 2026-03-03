import streamlit as st
from langgraph1_backend import workflow
from langchain_core.messages import HumanMessage
import uuid

# ******************* Utility function to generate unique thread IDs *******************
def generate_thread_id():
    thread_id=uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    config={'configurable':{ 'thread_id': thread_id}}
    return workflow.get_state(config=config).values['messages']

def get_conversation_title(thread_id):
    try:
        messages = load_conversation(thread_id)
        for msg in messages:
            if isinstance(msg, HumanMessage):
                # First user message → title
                return msg.content.strip().split("\n")[0][:60]
    except:
        pass
    return f"Chat {str(thread_id)[:8]}"


#  ******************* Initialize session state for message history *******************
if 'message_history' not in st.session_state:
        st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads']=[]

add_thread(st.session_state['thread_id'])

# ******************* Configuration for the workflow execution *******************
config={'configurable':{ 'thread_id': st.session_state['thread_id']}}

        
# ******************* Sidebar for the chat application *******************
st.sidebar.title("LangGraph ChartBoat")
if st.sidebar.button("New Chart"):
    reset_chat()
st.sidebar.header("MY Conversations")
for thread_id in st.session_state['chat_threads']:  # most recent first
    title = get_conversation_title(thread_id)

    if st.sidebar.button(title, help=title):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_messages = []
        for message in messages:
            role = "user" if isinstance(message, HumanMessage) else "assistant"
            temp_messages.append(
                {"role": role, "content": message.content}
            )

        st.session_state['message_history'] = temp_messages


# ******************* Displaying the conversation history *******************
for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])
    

# ******************* Input box for user messages *******************
user_input =st.chat_input("Type your message here...")

# ******************* Handling user input and generating AI response *******************
if user_input:

    # first add the user message to the history
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    
  

# ******************* Stream the AI response and update the conversation history *******************
    with st.chat_message("assistant"):
      
      ai_message=st.write_stream(
          message_chunk.content for message_chunk,metadata in  workflow.stream(
              {'messages': st.session_state['message_history']},
                config=config,
                stream_mode="messages"
          )
      )

    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})