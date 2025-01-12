from groq import Groq
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import streamlit as st

qdrant_client = QdrantClient(url="https://356b0073-43ff-431b-869c-3323795ecd9e.europe-west3-0.gcp.cloud.qdrant.io:6333",
                            api_key=st.secrets["QdrantAPI"])
groq_client = Groq(api_key = st.secrets["GroqAPI"])
collection_name = "iitd_knowledge"
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def respond(query):
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
    
    return response.choices[0].message.content

def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def main():
    st.header("Welcome to Your Ultimate Campus Companion: IIT Delhi AI Assistant")
    st.text("Embarking on your journey at IIT Delhi can be as thrilling as it is challenging. That’s where our AI Assistant steps in! Designed to simplify, guide, and enrich every aspect of your campus life, this intelligent tool is your go-to companion for everything IIT Delhi has to offer.")
    
    # Initialize session state
    initialize_session_state()
    
    # Display chat history
    display_chat_history()
    
    # Chat input
    prompt = st.text_area("What's your query?")
    if st.button("Enter"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get bot response (replace this with your actual response generation logic)
        response = respond(prompt)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)

if __name__ == "__main__":
    main()
