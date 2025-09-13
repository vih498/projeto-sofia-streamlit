import tempfile
import streamlit as st
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

def show():
    st.title("Análise de Documentos com Groq")

# ---------- Campo para digitar a chave da Groq ----------
    api_key = st.text_input("Chave Groq", type="password", placeholder="Digite sua chave da Groq")

# ---------- Upload de arquivos ----------
    uploaded_files = st.file_uploader(
        "Envie seus documentos (PDF ou TXT)",
        type=["pdf", "txt"],
        accept_multiple_files=True
    )

# ---------- Verificações ----------
    if not api_key:
        st.warning("Digite a chave da Groq para prosseguir.")
        return

    if not uploaded_files:
        st.info("Envie pelo menos um documento para análise.")
        return

# ---------- Definir chave Groq ----------
    import os
    os.environ["GROQ_API_KEY"] = api_key

# ---------- Carregar conteúdo dos documentos ----------
    textos = ""
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file.type.split('/')[-1]}") as tmp_file:
            tmp_file.write(file.read())
            tmp_path = tmp_file.name

        if file.type == "application/pdf":
            loader = PyPDFLoader(tmp_path)
        else:
            loader = TextLoader(tmp_path)

        docs = loader.load()
        for doc in docs:
            textos += doc.page_content + "\n"

    st.success(f"{len(uploaded_files)} documento(s) carregado(s) com sucesso!")

# ---------- Inicializar modelo Groq ----------
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)

# ---------- Pergunta do usuário ----------
    pergunta = st.text_input("Digite sua pergunta sobre os documentos:")
    if pergunta:
        prompt = f"Considere os seguintes documentos:\n{textos}\n\nPergunta: {pergunta}"
        with st.spinner("Buscando resposta..."):
            resposta = llm([HumanMessage(content=prompt)])
        st.markdown(f"**Resposta:** {resposta.content}")