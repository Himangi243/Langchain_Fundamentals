from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model='',dimentions=32) #jitna small vector utna kam contexual meaning capture karega 
documents=[
    "delhi is the capital of india ",
    "kolkata is the capital of West bengal",
    "paris is the capital of france"
]


result=embedding.embed_documents("delhi is the capital of india")

print(str(result))
#code  for generating  embedding for  any documents 

