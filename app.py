import streamlit as st

from query import ask

st.set_page_config(page_title="HR Policy Chatbot")

st.title("HR Policy Assistant")

question = st.text_input("Ask a HR Question")

if st.button("Ask"):

    answer, docs = ask(question)

    st.subheader("Answer")

    st.write(answer)

    st.subheader("Sources")

    for doc in docs:

        st.write(doc.metadata["source"])