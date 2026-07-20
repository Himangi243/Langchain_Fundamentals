from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)


chat_model = ChatHuggingFace(llm=llm)

parser=JsonOutputParser()
template=PromptTemplate(
    template="give me the name ,age and city of the fictional person \n{format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}# this is the partial variable because it is not filling on run time filed before runtime using function call
)

prompt=template.format()
print(prompt)


result=chat_model.invoke(prompt)
#print(result)


final_result=parser.parse(result.content)
print(final_result)

#using chains
#chain= template | chat_model |  parser
#result=chain.invoke({#here you input or blank dictionary})
#print(result)