from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch ,RunnableLambda,RunnableSequence
from pydantic import BaseModel ,Field
from typing import Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()


prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1 , chat_model ,parser ),
    'linkedin':RunnableSequence( prompt2 ,chat_model,parser)
  })

result=parallel_chain.invoke({'topic':'AI'})
#print(result)
print(result['tweet'])
print(result['linkedin'])
