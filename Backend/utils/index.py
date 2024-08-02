import os
from dotenv import load_dotenv
from pinecone import ServerlessSpec, Pinecone

load_dotenv()

os.environ['PINECONE_API_KEY']=os.getenv('PINECONE_API_KEY')

class Index(object):
    def __init__(self) -> None:
        self.pinecone=Pinecone()
        self.dimension=256
    
    
    def createIndex(self, indexName:str)->None:
        self.pinecone.create_index(
            name=indexName,
            dimension=self.dimension,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    
    def deleteIndex(self, indexName:str)->None:
        self.pinecone.delete_index(name=indexName)
    
        