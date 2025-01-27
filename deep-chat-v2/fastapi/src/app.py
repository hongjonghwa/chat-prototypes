from fastapi import Request,Body, FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from services.chat import Chat
from models.chat import ChatBody
from dotenv import load_dotenv

# ------------------ SETUP ------------------

load_dotenv()

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

chat_service = Chat()

@app.get("/")
def read_root():
    return ""


@app.post("/chat")
def chat(body: ChatBody):
    print('request', body)
    return chat_service.chat(body)


@app.post("/chat-stream")
def chat_stream(body: ChatBody):
    print('request', body)
    return chat_service.chat_stream(body)



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}