import os
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
from langchain.prompts import ChatPromptTemplate


load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')

class Chain(object):
    def __init__(self) -> None:
        self.llm=ChatGroq(model="llama3-8b-8192",
                          temperature=0.7)
        
        
    def getChain():
        pass
        
    



