import streamlit as st
import re
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from views.login import check_login

def limpar_resposta(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

def show():
    check_login()
    api_key = st.session_state.api_key

    st.title("Geração de Conteúdo")

    pergunta = st.text_input(
        "O que você quer saber?",
        placeholder="Digite aqui sua pergunta ou assunto"
    )

    if pergunta.strip():
        try:
            llm = ChatGroq(
                model="deepseek-r1-distill-llama-70b",
                groq_api_key=api_key
            )

            prompt_template = ChatPromptTemplate.from_messages([
                ("system", "Você é um professor especialista em educação."),
                ("user", "Crie um conteúdo didático sobre: {pergunta}.")
            ])

            chain = prompt_template | llm

            with st.spinner("Gerando conteúdo..."):
                resultado = chain.invoke({"pergunta": pergunta})
                resultado = limpar_resposta(resultado.content)

            st.success("Conteúdo gerado com sucesso!")
            st.write("### Resultado")
            st.write(resultado)

        except Exception as e:
            st.error(f"Erro ao gerar conteúdo: {e}")