import streamlit as st

st.title("Flashcard Application")
st.write("Welcome to the Flashcard Application!")
name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello, {name}! How can I help you?")