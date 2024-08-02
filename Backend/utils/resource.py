import os
from dotenv import load_dotenv
from pinecone import ServerlessSpec, Pinecone
from langchain.vectorstores import Pinecone as PineconeVectorStore

load_dotenv()

os.environ['PINECONE_API_KEY']=os.getenv('PINECONE_API_KEY')

class Resource(object):
    def __init__(self) -> None:
        pass
    
    
    def createIndex(self, indexName:str):
        pass
    
    def deleteIndex(self, indexName:str):
        pass
    
    def updateIndex(self, indexName:str):
        pass