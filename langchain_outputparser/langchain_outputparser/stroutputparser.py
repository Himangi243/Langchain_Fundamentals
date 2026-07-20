from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

#1st prompt -> detailed report
template1=PromptTemplate(
    template= "write detailed report on {topic}",
    input_variables=['topic']

)



#2nd prompt -> summary
template2=PromptTemplate(
    template= "write a 5 line summary on the following text. /n {topic}",
    input_variables=['topic']
)

prompt1=template1.invoke({"topic":"black hole"})

result=chat_model.invoke(prompt1)

prompt2=template2.invoke({'topic':result.content})

result1=chat_model.invoke(prompt2)
print(result1.content)