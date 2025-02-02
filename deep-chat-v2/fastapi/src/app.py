import config
from fastapi import Request,Body, FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
import os

from services.fake_chat import FakeChat
from models import ChatRequestBody

from langchain_openai import ChatOpenAI
from agents.openai import ChatAgent
import logging

# ------------------ SETUP ------------------

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ EXCEPTION HANDLERS ------------------

# Sends response back to Deep Chat using the Response format:
# https://deepchat.dev/docs/connect/#Response

@app.exception_handler(Exception)
def handle_exception(e):
    print(e)
    return {"error": str(e)}, 500

# ------------------ API ------------------

fake_chat_service = FakeChat()
openai_agent = ChatAgent()

@app.get("/")
def read_root():
    return ""


@app.post("/chat")
def chat(body: ChatRequestBody):
    logging.info('request', body)
    return fake_chat_service.chat(body)


@app.post("/chat-stream")
def chat_stream(body: ChatRequestBody):
    logging.info('request', body)
    message = body.messages[-1].text.strip()
    if message == "":
        return 200
    
    return openai_agent.chat_stream(body)
    # return fake_chat_service.chat_stream(body)



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}