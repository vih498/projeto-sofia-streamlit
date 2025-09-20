import tempfile
import streamlit as st
import pandas as pd
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from views.login import check_login

def show():
    check_login()
    api_key = st.session_state.api_key

    st.title("Análise de Documentos")

    uploaded_files = st.file_uploader(
        "Envie seus documentos (PDF, TXT ou Excel)",
        type=["pdf", "txt", "xlsx", "xls"],
        accept_multiple_files=True
    )

    if not uploaded_files:
        st.info("Envie pelo menos um documento para análise.")
        return

    textos = ""
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file.name.split('.')[-1]}") as tmp_file:
            tmp_file.write(file.read())
            tmp_path = tmp_file.name

        if file.type == "application/pdf" or file.name.endswith(".pdf"):
            loader = PyPDFLoader(tmp_path)
            docs = loader.load()
            for doc in docs:
                textos += doc.page_content + "\n"
        elif file.type.startswith("text") or file.name.endswith(".txt"):
            loader = TextLoader(tmp_path)
            docs = loader.load()
            for doc in docs:
                textos += doc.page_content + "\n"
        elif file.name.endswith((".xlsx", ".xls")):
            df_excel = pd.read_excel(tmp_path)
            textos += "\n".join(df_excel.astype(str).apply(lambda row: " | ".join(row), axis=1)) + "\n"

    st.success(f"{len(uploaded_files)} documento(s) carregado(s) com sucesso!")

    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.7,
        groq_api_key=api_key
    )

    pergunta = st.text_input("Digite sua pergunta sobre os documentos:")
    if pergunta:
        prompt = f"Considere os seguintes documentos:\n{textos}\n\nPergunta: {pergunta}"
        with st.spinner("Buscando resposta..."):
            resposta = llm([HumanMessage(content=prompt)])
        st.markdown(f"**Resposta:** {resposta.content}")