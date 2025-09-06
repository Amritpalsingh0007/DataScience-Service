from utils.message_util import MessageUtil
from service.llm_service import LLMService

class MessageService:
    def __init__(self):
        self.message_util = MessageUtil()
        self.llm_service = LLMService()
    
    def process_message(self, message: str):
        if self.message_util.isBankSms(message):
            return self.llm_service.runLLM(message)
        return None