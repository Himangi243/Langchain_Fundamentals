from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',#directory ka path
    glob='*.pdf',# folder ke ander se konsi file ko load karna hai-> pattern 
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)