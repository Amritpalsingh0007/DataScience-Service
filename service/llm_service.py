import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

from models.expense import Expense

class LLMService:
    def __init__(self):
        load_dotenv()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", 
                 "You are a expert extraction algorithm."
                 "Only extract relevant information from the text."
                 "If you do not know the value of an attribute asked to extract, "
                 "return null for the attribute value"
                ),
                ("human", "{text}")
            ]
        )
        self.apikey = os.getenv("GOOGLE_API_KEY")
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        self.chain = self.prompt | self.llm.with_structured_output(schema=Expense)
    
    def runLLM(self, message: str):
        return self.chain.invoke({"text":message})