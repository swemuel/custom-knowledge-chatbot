import openai
import os
from llama_index import SimpleDirectoryReader
from llama_index import VectorStoreIndex

os.environ['OPENAI_API_KEY'] = "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"
# Set your OpenAI API key
openai.api_key = "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"

# Load you data into 'Documents' a custom type by LlamaIndex
documents = SimpleDirectoryReader('./data').load_data()

# Create index for your documents
index = VectorStoreIndex.from_documents(documents)

# Create a query engine from the index
query_engine = index.as_query_engine()

# Query test
response = query_engine.query("What do you think of Facebook's LLaMa?")

print(response)