from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch ,RunnableLambda,RunnableSequence ,RunnablePassthrough
from pydantic import BaseModel ,Field
from typing import Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt1 =PromptTemplate(
    template='write a joke about {topic}',
    input_variables={'topic'}
)
prompt2=PromptTemplate(
    template='explain the following joke-{text} ',
    input_variables={'text'}
)

joke_gen_chain=RunnableSequence(prompt1 ,chat_model ,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,chat_model,parser)
})

final_chain=RunnableSequence(joke_gen_chain ,parallel_chain)

print(final_chain.invoke({'topic':'dragons'}))