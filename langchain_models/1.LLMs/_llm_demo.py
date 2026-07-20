from langchain_openai import  OpenAI #integeration pakage between langchain and openai
from dotenv import load_dotenv # dot env apki env file se secret keys ko load karta hai current file mein

load_dotenv()    # loading api key

llm=OpenAI(model="gpt-4o-mini") # making object of openai 
result=llm.invoke("what is the capital of india")#very importand function in langchain -invoke helps to communicate with this model  
print(result)
# i/p plain textv(string)-->llm --> plaintext(string) o/p