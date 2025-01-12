import streamlit as st

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
        response = f"Echo: {prompt}"  # Placeholder response
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)

if __name__ == "__main__":
    main()
