import os
import faiss
import numpy as np
import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import logging

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

# Sample test documents
documents = [
    "How to deploy a Kubernetes service?",
    "Guide to setting up a PostgreSQL database.",
    "Introduction to machine learning algorithms.",
    "Best practices for writing Python code.",
    "How to configure a Nginx web server?",
    "Troubleshooting Docker container issues.",
    "A beginner's guide to Git and GitHub.",
    "Steps to optimize SQL queries for performance.",
    "Understanding RESTful API design principles.",
    "How to integrate CI/CD pipelines with Jenkins.",
    "Introduction to cloud computing with AWS.",
    "Basic Linux commands every developer should know.",
    "How to secure web applications from cyber threats?",
    "A complete guide to web scraping with Python.",
    "The fundamentals of object-oriented programming.",
    "Deploying machine learning models in production.",
    "How to automate repetitive tasks using Python scripts.",
    "Understanding NoSQL databases like MongoDB.",
    "A guide to writing unit tests in JavaScript.",
    "How to use GraphQL for efficient API development."
]

# Generate OpenAI embeddings for documents
def get_embedding(text):
    response = openai.embeddings.create(
        input=text, model="text-embedding-ada-002"
    )
    return np.array(response.data[0].embedding, dtype=np.float32)

embeddings = np.array([get_embedding(doc) for doc in documents], dtype=np.float32)

# Create FAISS index
d = embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)

# Initialize Slack App
app = App(token=SLACK_BOT_TOKEN)

# Function to search FAISS
def search_faiss(query):
    query_vector = np.array([get_embedding(query)], dtype=np.float32)
    faiss.normalize_L2(query_vector)
    _, idx = index.search(query_vector, k=1)
    return documents[idx[0][0]]

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
