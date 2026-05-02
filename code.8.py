#Make it a Web App (Streamlit UI)
import streamlit as st

st.title("🤖 Study AI Agent")

user_input = st.text_input("Ask something:")

if user_input:
    response = agent(user_input)
    st.write(response)
    