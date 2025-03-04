from faiss import IndexFlatL2
from langchain import hub
from langchain.chat_models import init_chat_model
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


# These functions assume os.environ["OPENAI_API_KEY"] is set
def load_embeddings(source_path:str = "coda_linear_github_embeddings.db"):
    embeddings = OpenAIEmbeddings()
    faiss = FAISS(embedding_function=embeddings,
                  index=IndexFlatL2,
                  docstore=InMemoryDocstore(),
                  index_to_docstore_id={})
    return faiss.load_local(folder_path=f"./db/{source_path}",
                            embeddings=embeddings,
                            allow_dangerous_deserialization=True)


def execute_query(question: str, embeddings:list = None, model:str = "gpt-4"):
    if embeddings is not None and len(embeddings) > 0:
        docs = embeddings.similarity_search(query=question, k=3)
        docs_content = "\n\n".join(doc.page_content for doc in docs)
    else:
        docs_content = ""
    prompt = hub.pull("rlm/rag-prompt")
    llm = init_chat_model(model, model_provider="openai")
    return llm.invoke(prompt.invoke({"question": question, "context": docs_content})).content
