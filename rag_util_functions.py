from enum import Enum
from faiss import IndexFlatL2
from langchain import hub
from langchain.chat_models import init_chat_model
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from pydantic import BaseModel
from typing import Optional


class Source(Enum):
    LINEAR = "Linear"
    CODA = "Coda"
    GITHUB = "Github"


source_db_map = {
    Source.LINEAR: "linear_embeddings.db",
    Source.CODA: "github_embeddings.db",
    Source.GITHUB: "coda_embeddings.db"
}


class SourceDBResponse(BaseModel):
    ranked_sources: list[Source]


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


def rank_sources(question: str, model: str = "gpt-4o"):
    llm = init_chat_model(model, model_provider="openai").with_structured_output(SourceDBResponse)
    result = llm.invoke(
        f"I have {Source.__len__()} data sources: {','.join([s.name for s in list(Source)])}. Order these from most to "
        f"least relevant for answering the following question: {question}")
    return result


def execute_query(question: str, embeddings_dbs: Optional[list[FAISS]] = None, model: str = "gpt-4o", k: int = 3):
    if embeddings_dbs is not None and len(embeddings_dbs) > 0:
        for embeddings_db in embeddings_dbs:
            docs = embeddings_db.similarity_search(query=question, k=k)
            docs_content = "\n\n".join(doc.page_content for doc in docs)
            if len(docs_content) > 0:
                break
    else:
        docs_content = ""
    prompt = hub.pull("rlm/rag-prompt")
    llm = init_chat_model(model, model_provider="openai")
    return llm.invoke(prompt.invoke({"question": question, "context": docs_content})).content


def query_preferred_source(question: str, model: str = "gpt-4o"):
    source_dbs = load_databases()
    sources = rank_sources(question).ranked_sources
    dbs = [source_dbs[s] for s in sources]
    return execute_query(question, dbs, model)


def query_all_sources(question: str, model: str = "gpt-4o", k: int = 3):
    dbs = load_databases()
    docs = []
    for db in dbs.values():
        docs += db.similarity_search(query=question, k=k)
    docs_content = "\n\n".join(doc.page_content for doc in docs)
    prompt = hub.pull("rlm/rag-prompt")
    llm = init_chat_model(model, model_provider="openai")
    return llm.invoke(prompt.invoke({"question": question, "context": docs_content})).content
