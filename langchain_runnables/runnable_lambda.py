"""from langchain_core.runnables import RunnableLambda
def word_counter(text):
    return len(text.split())
runnable_word_counter=RunnableLambda(word_counter)
print(runnable_word_counter.invoke('hi there how are you ?'))"""



from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch ,RunnableLambda,RunnableSequence ,RunnablePassthrough,RunnableLambda
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
def word_count(text):
    return len(text.split())
joke_gen_chain=RunnableSequence(prompt1 ,chat_model ,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_gen_chain ,parallel_chain)

result=final_chain.invoke({'topic':'dragons'})
final_result="""{} \n word count -{}""".format(result['joke'],result['word_count'])
print(final_result)