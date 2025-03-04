import os
import json
import faiss
import numpy as np
import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import logging
from collections import deque
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain import hub
from langchain.chat_models import init_chat_model
from langchain.embeddings import OpenAIEmbeddings
from faiss import IndexFlatL2
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from openai import OpenAI
from llm_tools import create_linear_ticket, tools 

# Load environment variables from .env file
load_dotenv()

print("SLACK_BOT_TOKEN:", os.getenv("SLACK_BOT_TOKEN"))
print("SLACK_APP_TOKEN:", os.getenv("SLACK_APP_TOKEN"))
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# Define API Keys and Tokens from environment variables
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LINEAR_API_KEY = os.environ.get("LINEAR_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Configure OpenAI API Key
openai.api_key = OPENAI_API_KEY
client = OpenAI()

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Memory storage for last 5 mentions
mention_memory = {}  # Key: channel_id, Value: deque of last 5 mentions

# Generate OpenAI embeddings for documents
def get_embedding(text):
    response = openai.embeddings.create(
        input=text, model="text-embedding-ada-002"
    )
    return np.array(response.data[0].embedding, dtype=np.float32)

# Initialize Slack App
app = App(token=SLACK_BOT_TOKEN)

def parse_chat_history(chat_history_raw):
    chat_history = []
    for message in chat_history_raw:
        chat_history.append({"role": "user", "content": message})
    return chat_history

def get_prompt_messages(chat_history, question, context):
    messages = [
        {"role": "developer", "content": "You are a helpful assistant."}, # update this system prompt more
    ]
    messages.extend(chat_history)
    messages.extend({"role": "developer", "content": f"This is the relevant context for you to answer the users query: {context}"})
    messages.extend({"role": "user", "content": question})
    return messages

def chat_openai(messages, tools, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

def implement_linear_function(function_args):
    function_args = json.loads(function_args)
    result = create_linear_ticket(
        title=function_args.get("title"),
        description=function_args.get("description"),
        priority=function_args.get("priority")
    )
    second_message = f"A ticket as been created here: {result['issue']['url']}"
    return second_message

# Function to search FAISS
def search_faiss(query, channel_id):
    embeddings = OpenAIEmbeddings()
    faiss = FAISS(embedding_function=embeddings, index=IndexFlatL2, docstore=InMemoryDocstore(), index_to_docstore_id={})
    db = faiss.load_local(folder_path="./db/coda_linear_github_embeddings.db", embeddings=embeddings, allow_dangerous_deserialization=True)

    docs = db.similarity_search(query, k=3)
    logging.debug(f"Len docs: {len(docs)}")

    docs_content = "\n\n".join(doc.page_content for doc in docs)
    logging.debug(f"Doc sources: {';'.join([d.metadata['source'] for d in docs])}")

    # Retrieve last 5 messages from memory for this channel
    # chat_history = "\n".join(mention_memory.get(channel_id, []))
    chat_history = mention_memory.get(channel_id, [])
    chat_history = parse_chat_history(chat_history)
    logging.debug(f"🔹 Chat History for channel {channel_id}: {chat_history}")

    messages = get_prompt_messages(chat_history, query, docs_content)
    response = chat_openai(messages, tools)

    if response.tool_calls != None:
        function_name = response.tool_calls[0].function.name
        function_args = response.tool_calls[0].function.arguments
        if function_name == "create_linear_ticket":
            try:
                response = implement_linear_function(function_args)
            except:
                response = "Sorry failed to create a ticket (still learning!) - can you ask again?"

    return response  # Fix: LLMChain outputs a string, no need for `.content`

# Function to store last 5 mentions per channel
def store_mention(channel_id, mention_text):
    if channel_id not in mention_memory:
        mention_memory[channel_id] = deque(maxlen=10)
    mention_memory[channel_id].append(mention_text)
    logging.debug(f"🔹 Updated memory for channel {channel_id}: {list(mention_memory[channel_id])}")

# Slack bot listens for messages that mention it
@app.event("app_mention")
def handle_mention(event, say):
    logging.debug(f"🔹 Received mention event: {event}")  # Debugging log
    user_query = event["text"]
    channel_id = event["channel"]
    
    store_mention(channel_id, user_query)  # Store the mention
    best_match = search_faiss(user_query, channel_id)
    logging.debug(f"🔹 Best FAISS match: {best_match}")
    
    say(f"Best Match: {best_match}")

# Start the Slack bot using Socket Mode
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
