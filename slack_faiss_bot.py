import os
import faiss
import numpy as np
import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import logging
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from faiss import IndexFlatL2

# Load environment variables from .env file
load_dotenv()

print("SLACK_BOT_TOKEN:", os.getenv("SLACK_BOT_TOKEN"))
print("SLACK_APP_TOKEN:", os.getenv("SLACK_APP_TOKEN"))
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# # Define API Keys and Tokens from environment variables
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



# Configure OpenAI API Key
openai.api_key = OPENAI_API_KEY

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)


# Generate OpenAI embeddings for documents
def get_embedding(text):
    response = openai.embeddings.create(
        input=text, model="text-embedding-ada-002"
    )
    return np.array(response.data[0].embedding, dtype=np.float32)


# Initialize Slack App
app = App(token=SLACK_BOT_TOKEN)

# Function to search FAISS
def search_faiss(query):
    embeddings = OpenAIEmbeddings()
    faiss = FAISS(embedding_function=embeddings, index=IndexFlatL2, docstore=InMemoryDocstore(), index_to_docstore_id={})    
    db = faiss.load_local(folder_path="./db/coda_linear_embeddings.db", embeddings=embeddings, allow_dangerous_deserialization=True)
    return db.similarity_search(query, k=5)

# Slack bot listens for messages that mention it
@app.event("app_mention")
def handle_mention(event, say):
    logging.debug(f"🔹 Received mention event: {event}")  # Debugging log
    user_query = event["text"]
    best_match = search_faiss(user_query)
    logging.debug(f"🔹 Best FAISS match: {best_match}")
    say(f"Best Match: {best_match}")

# Start the Slack bot using Socket Mode
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
