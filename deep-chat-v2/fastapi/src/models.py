from pydantic import BaseModel


# ------------------ SETUP ------------------


# ------------------ Deep Chat 2.1.1 ------------------
# https://github.com/OvidijusParsiunas/deep-chat

class MessageFile(BaseModel):
    name: str
    src: str
    type: str
    #ref: File # ??


class MessageContent(BaseModel):
    role: str
    text: str
    #files: list[MessageFile] | None = None 
    #html : str | None = None

class ChatRequestBody(BaseModel):
    messages: list[MessageContent]
    customBodyField: str | None = None