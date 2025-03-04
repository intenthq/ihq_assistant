import os

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

os.environ["OPENAI_API_KEY"] = "<your key>"

file_base_path = "./documents"
data_folders = ["coda", "linear"]

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

txt_file_path = './documents/coda/AI-Powered_Insights_Hub.md'
docs = []
for folder in data_folders:
    for file in os.listdir(f"{file_base_path}/{folder}"):
        loader = TextLoader(file_path=f"{file_base_path}/{folder}/{file}", encoding="utf-8")
        data = loader.load()
        docs += text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding=embeddings)
vectorstore.save_local("./db/coda_linear_embeddings.db")