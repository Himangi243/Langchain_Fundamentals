from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

parser=StrOutputParser()
# chains - pipeline entire flow
chain=template1 | chat_model | parser | template2 | chat_model | parser
result=chain.invoke({'topic':'black hole'})

print(result)