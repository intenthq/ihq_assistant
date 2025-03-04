import os
import faiss
import numpy as np
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from sklearn.feature_extraction.text import TfidfVectorizer

# Load documents
documents = np.load("documents.npy", allow_pickle=True).tolist()

# Load FAISS index
index = faiss.read_index("faiss_test_index.bin")

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
vectorizer.fit(documents)  # Fit the vectorizer on the documents

# Slack Bot Tokens
SLACK_BOT_TOKEN = "<your-token>"
SLACK_APP_TOKEN = "<your-token>"

# Initialize Slack App
app = App(token=SLACK_BOT_TOKEN)

# Function to search FAISS
def search_faiss(query):
    query_vector = vectorizer.transform([query]).toarray().astype(np.float32)
    faiss.normalize_L2(query_vector)
    _, idx = index.search(query_vector, k=1)
    return documents[idx[0][0]]

# Slack bot listens for messages that mention it
@app.event("app_mention")
def handle_mention(event, say):
    user_query = event["text"]
    # best_match = search_faiss(user_query)
    say(f"📌 Best Match: {user_query}")

# Start the Slack bot using Socket Mode
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
