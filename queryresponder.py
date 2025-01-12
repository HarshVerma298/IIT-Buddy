from groq import Groq
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# Your existing retrieval code
qdrant_client = QdrantClient(url="https://356b0073-43ff-431b-869c-3323795ecd9e.europe-west3-0.gcp.cloud.qdrant.io:6333",
                            api_key=userdata.get("QDRANTAPI"))
groq_client = Groq(api_key = userdata.get("GroqAPI2"))
collection_name = "iitd_knowledge"

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
query = "give suggestions regarding foreign intern for an iitd student"
query_vector = embedding_model.encode(query).tolist()

search_results = qdrant_client.search(
    collection_name=collection_name,
    query_vector=query_vector,
    limit=20,
    with_payload=True
)

retrieved_context = "\n".join([result.payload['txt'] for result in search_results])
prompt = f"""You are a knowledgeable AI assistant. Use the information below to help answer the user's question. 
        Provide a natural, conversational response without mentioning or referring to the context or sources.
        If you cannot answer based on the information provided, provide a general response while staying within your knowledge domain.

        Information: {retrieved_context}

        Human: {query}

        Assistant:"""

# Groq API call

response = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant. Provide natural, conversational responses without referring to any context or sources."},
        {"role": "user", "content": prompt}
    ],
    temperature=1,
    max_tokens=10000,
    top_p=1,
    stream=False
)

print(response.choices[0].message.content)
