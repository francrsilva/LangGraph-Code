from agentic_chatbot_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage

thread_id = "1"
config = {'configurable': {'thread_id': thread_id}}

response = chatbot.invoke({'messages': [HumanMessage(content='What is Python?')]})

print(response['message'][-1].content)
