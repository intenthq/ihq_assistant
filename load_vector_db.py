import os

from faiss import IndexFlatL2
from langchain import hub
from langchain.chat_models import init_chat_model
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = "<your key>"

embeddings = OpenAIEmbeddings()
faiss = FAISS(embedding_function=embeddings, index=IndexFlatL2, docstore=InMemoryDocstore(), index_to_docstore_id={})
db = faiss.load_local(folder_path="./db/coda_linear_embeddings.db",
                      embeddings=embeddings,
                      allow_dangerous_deserialization=True)

llm = init_chat_model("gpt-4", model_provider="openai")

question = "What is the IHQ Graph"

docs = db.similarity_search(query=question, k=3)
docs_content = "\n\n".join(doc.page_content for doc in docs)

prompt = hub.pull("rlm/rag-prompt")

response = llm.invoke(prompt.invoke({"question": question, "context": docs_content}))
print(response.content)
