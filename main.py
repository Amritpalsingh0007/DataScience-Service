from fastapi import FastAPI
from models.message import Message
from service.message_service import MessageService

app = FastAPI()

message_service = MessageService()

@app.post("/ds/v1/message")
def hangle_message(message: Message):
    return message_service.process_message(message.message)