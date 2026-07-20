from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

import os 

os.environ['HF_HOME']='D:/huggingface_cache'
#just to store folder in  d drive

llm=HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation',
    pipeline_kwargs=dict(
        tenperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)
result=model.invoke(" what is the capital of india")
print(result.content)
