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
prompt1 = PromptTemplate(
    template= 'generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= 'generate a 5 pointer summary on {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()
chain= prompt1 | chat_model | parser | prompt2 |chat_model | parser 
result=chain.invoke({'topic':'unemployment in india'})
print(result)
chain.get_graph().print_ascii()