from fastapi import Request,Body, FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from services.chat import FakeChat, ChatService
from models import ChatRequestBody
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# ------------------ SETUP ------------------

load_dotenv()
print(os.environ.get("OPENAI_API_KEY"))
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key = os.environ.get("OPENAI_API_KEY"))
# 
# print(os.environ.get("OPENAI_API_KEY"))

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
chat_service = ChatService()

@app.get("/")
def read_root():
    return ""


@app.post("/chat")
def chat(body: ChatRequestBody):
    print('request', body)
    return fake_chat_service.chat(body)


@app.post("/chat-stream")
def chat_stream(body: ChatRequestBody):
    print('request', body)
    return fake_chat_service.chat_stream(body)



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}