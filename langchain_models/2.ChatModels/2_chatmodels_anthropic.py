# just like  open ai claude is also paid  to get api keys
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
model = ChatAnthropic(MODEL="claude-3-5-sonnet-2241022")# we can set temperature and  completion tokens
result= model.invoke('what is the capital of india')
print(result.content)
# code to communicate with claude api