import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import re

def limpar_resposta(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

def show():
    st.title("Geração de Conteúdo com IA")

    # Entrada da chave do usuário
    api_key = st.text_input("Digite sua chave da Groq", type="password")

    with st.form("conteudo_form"):
        titulo = st.text_input("Título do Conteúdo")
        tema = st.text_area("Tema/Assunto")
        gerar = st.form_submit_button("Gerar")

    if gerar:
        if not api_key:
            st.error("Você precisa informar a chave da Groq.")
        elif not titulo.strip() or not tema.strip():
            st.warning("Preencha o título e o tema.")
        else:
            try:
                # Inicializa o modelo ChatGroq
                llm = ChatGroq(
                    model="deepseek-r1-distill-llama-70b",
                    groq_api_key=api_key
                )

                # Prompt template
                prompt_template = ChatPromptTemplate.from_messages([
                    ("system", "Você é um professor especialista em educação."),
                    ("user", "Crie um conteúdo didático sobre o tema: {tema}, com título: {titulo}.")
                ])

                # Conecta prompt ao modelo
                chain = prompt_template | llm  # Aqui o LLM gera o texto

                with st.spinner("Gerando conteúdo..."):
                    resultado = chain.invoke({"titulo": titulo, "tema": tema})
                    resultado = limpar_resposta(resultado.content)

                st.success("Conteúdo gerado com sucesso!")
                st.write("### Resultado")
                st.write(resultado)

            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")