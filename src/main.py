import uvicorn
from fastapi import FastAPI
from models.message import Message
from service.message_service import MessageService
from kafka import KafkaProducer
import json
import os

app = FastAPI()

message_service = MessageService()

KAFKA_HOST = os.getenv('KAFKA_HOST', 'localhost')
KAFKA_PORT = os.getenv('KAFKA_PORT', '9092')
producer = KafkaProducer(bootstrap_servers=[f'{KAFKA_HOST}:{KAFKA_PORT}'],
                         value_serializer=lambda v : json.dumps(v).encode('utf-8'))

@app.post("/ds/v1/message")
def hangle_message(message: Message):
    result = message_service.process_message(message.message)
    producer.send('expense_service', result.model_dump())
    return result

@app.get("/")
def hello_World():
    return "Hello World!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)