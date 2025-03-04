from faiss import IndexFlatL2
from langchain import hub
from langchain.chat_models import init_chat_model
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from typing import Optional

source_db_map = {
    "linear": "linear_embeddings.db",
    "github": "github_embeddings.db",
    "coda": "coda_embeddings.db"
}


# These functions assume os.environ["OPENAI_API_KEY"] is set
def load_embeddings(source_path: str = "coda_linear_github_embeddings.db"):
    embeddings = OpenAIEmbeddings()
    faiss = FAISS(embedding_function=embeddings,
                  index=IndexFlatL2,
                  docstore=InMemoryDocstore(),
                  index_to_docstore_id={})
    return faiss.load_local(folder_path=f"./db/{source_path}",
                            embeddings=embeddings,
                            allow_dangerous_deserialization=True)


def load_databases():
    dbs = {}
    embeddings = OpenAIEmbeddings()
    faiss = FAISS(embedding_function=embeddings,
                  index=IndexFlatL2,
                  docstore=InMemoryDocstore(),
                  index_to_docstore_id={})
    for source in source_db_map.keys():
        dbs[source] = faiss.load_local(folder_path=f"./db/{source_db_map[source]}",
                                       embeddings=embeddings,
                                       allow_dangerous_deserialization=True)
    return dbs


def rank_sources(question: str, model: str = "gpt-4"):
    llm = init_chat_model(model, model_provider="openai")
    result = llm.invoke(
        "I have 3 data sources: coda, linear and github. Produce a comma-separated list ordering these from most to "
        f"least relevant for answering the following question: {question}")
    return [r.strip() for r in result.content.lower().split(",")]


def execute_query(question: str, embeddings_db: Optional[FAISS] = None, model: str = "gpt-4"):
    if embeddings_db is not None:
        docs = embeddings_db.similarity_search(query=question, k=3)
        docs_content = "\n\n".join(doc.page_content for doc in docs)
    else:
        docs_content = ""
    prompt = hub.pull("rlm/rag-prompt")
    llm = init_chat_model(model, model_provider="openai")
    return llm.invoke(prompt.invoke({"question": question, "context": docs_content})).content


def query_preferred_source(question: str, model: str = "gpt-4"):
    source_dbs = load_databases()
    db = source_dbs[rank_sources(question)[0]]
    return execute_query(question, db, model)