from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model="gpt-4",temperature=0.3,max_completion_tokens=10)
# max_completion_token -> how many tokens or word we need in our outputs
# temperature is the parameter that control the randomness of a language models output it affects how creative or deterministic the response are .. lower value(0.0-0.3)->(more deterministic and predictable) higher value (0.7-1.5) -> more random creative and diverse 
result =model.invoke("what is the capital of india?")
print(result)
# this time the result will not be simple plain text  there will be many other additional details with the ans given in content
print(result.content) # it will just return the ans 
