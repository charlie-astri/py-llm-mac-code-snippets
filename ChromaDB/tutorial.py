#  Create a Chroma Client
import chromadb
chroma_client = chromadb.Client()

# Create a collection
collection = chroma_client.create_collection(name="my_collection")

# Add some text documents to the collection
collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

# Query the collection
results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)

# Inspect Results
# {
#   'documents': [[
#       'This is a document about pineapple',
#       'This is a document about oranges'
#   ]],
#   'ids': [['id1', 'id2']],
#   'distances': [[1.0404009819030762, 1.243080496788025]],
#   'uris': None,
#   'data': None,
#   'metadatas': [[None, None]],
#   'embeddings': None,
# }
