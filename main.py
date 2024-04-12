from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import ChatMessage
from langchain_core.messages import HumanMessage, SystemMessage
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
def get_chat(question):
    model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0, max_tokens=1024)
    chat = ChatAnthropic(temperature=0, model_name="claude-3-opus-20240229")
    messages = [
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(content=question),
    ]
    chat.invoke(messages)
    for chunk in chat.stream(messages):
        return print(chunk.content, end="", flush=True)


app = FastAPI()
class InputData(BaseModel):
    humanMessage: str

@app.post("/chat")
def SendingData(data:InputData):
    question = data.name
    get_chat(question)
    
