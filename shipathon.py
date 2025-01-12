
import streamlit as st


st.header("Welcome to Your Ultimate Campus Companion: IIT Delhi AI Assistant")
st.text("Embarking on your journey at IIT Delhi can be as thrilling as it is challenging. That’s where our AI Assistant steps in! Designed to simplify, guide, and enrich every aspect of your campus life, this intelligent tool is your go-to companion for everything IIT Delhi has to offer.")

name = st.text_input("Enter your query")
if st.button("Enter"):
  if name:
    st.write(f"Getting to your query, {name}!")
