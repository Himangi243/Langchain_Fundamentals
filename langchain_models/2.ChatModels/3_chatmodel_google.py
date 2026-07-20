
from langchain_anthropic import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(MODEL="gemini-1.5-pro")# we can set temperature and  completion tokens
result= model.invoke('what is the capital of india')
print(result.content)
# code to communicate with gemini api