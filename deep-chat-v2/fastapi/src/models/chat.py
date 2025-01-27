from pydantic import BaseModel


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

class ChatBody(BaseModel):
    messages: list[MessageContent]
    customBodyField: str | None = None