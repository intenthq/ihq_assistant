import os

from faiss import IndexFlatL2
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = "<your key>"

embeddings = OpenAIEmbeddings()
faiss = FAISS(embedding_function=embeddings, index=IndexFlatL2, docstore=InMemoryDocstore(), index_to_docstore_id={})
db = faiss.load_local(folder_path="./db/coda_linear_embeddings.db", embeddings=embeddings, allow_dangerous_deserialization=True)

db.similarity_search("What is the IHQ Graph", k=5)