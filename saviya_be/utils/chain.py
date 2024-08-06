import os
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate,HumanMessagePromptTemplate,SystemMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

class Chain(object):
    def __init__(self) -> None:
        self.llm = ChatGroq(model="llama3-8b-8192", temperature=0.7)
    
    def getChain(self, question: str):
        template = """Given the following context and a question, generate an answer based on this context only.
                      In the answer try to provide as much text as possible from the "response" section in the source document context without making much changes.
                      If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

                      CONTEXT: {context}

                      QUESTION: {question}"""
                            
        chatPromptTemplate = ChatPromptTemplate.from_template(template=template)
        output_parser = StrOutputParser()
 
        chain = (
            chatPromptTemplate
            | self.llm
            | output_parser
        )
        
        return chain.invoke({"context": question, "question": question})
    

def main():
    chain = Chain()
    d = chain.getChain(question="What is the capital of Nigeria?")
    print(d)

if __name__ == "__main__":
    main()
