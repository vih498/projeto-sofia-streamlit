import streamlit as st
import re
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from views.login import check_login

def show():
    check_login()
    api_key = st.session_state.api_key

    st.title("Tradutor")

    idioma = st.text_input(
        "Idioma de destino",
        placeholder="Digite o idioma desejado (ex: Inglês, Espanhol, Francês, Italiano...)",
        key="tradutor_idioma"
    )
    texto_usuario = st.text_input(
        "Digite seu texto aqui e pressione Enter para traduzir",
        key="tradutor_texto"
    )

    if texto_usuario.strip() and idioma.strip():
        try:
            model = ChatGroq(
                model="deepseek-r1-distill-llama-70b",
                groq_api_key=api_key
            )

            mensagens = [
                SystemMessage(f"Traduza o texto a seguir para {idioma}:"),
                HumanMessage(texto_usuario)
            ]

            parser = StrOutputParser()
            chain = model | parser
            resultado = chain.invoke(mensagens)
            resultado_limpo = re.sub(r"<think>.*?</think>", "", resultado, flags=re.DOTALL).strip()

            st.write("### 🌍 Tradução:")
            st.success(resultado_limpo)
        except Exception as e:
            st.error(f"Erro: {e}")