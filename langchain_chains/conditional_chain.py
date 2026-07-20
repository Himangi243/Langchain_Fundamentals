from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch ,RunnableLambda
from pydantic import BaseModel ,Field
from typing import Literal
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
chat_model = ChatHuggingFace(llm=llm)
parser =StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal['positive','negative']= Field(description ='give the sentiment of the feedback')

parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template='classify the sentiment of the following feedaback text into positive or neagative \n{feedback}  \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)


classifier_chain = prompt1 | chat_model | parser2


#print(classifier_chain.invoke({'feedback':'this is the terrible smartphone'}))


# using pydantic output parser so that the output would be consistent
#for branching we have to import runnablebranch

prompt2=PromptTemplate(
    template='write a appropriate respose to this positive feedback \n {feedback}',
    input_variables=['feedback']

)
prompt3=PromptTemplate(
    template='write a appropriate respose to this negative feedback \n {feedback}',
    input_variables=['feedback']
    
)
"""branch_chain=RunnableBranch(
    (condition,chain1),
    (condition,chain2),
    default_chain
)"""
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | chat_model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | chat_model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()