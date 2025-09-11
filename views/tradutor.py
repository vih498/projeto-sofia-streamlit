import streamlit as st
import re
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

def show():
    st.title("Tradutor com Groq")

    # Formulário isolado do Tradutor
    with st.form(key="tradutor_form"):
        # Solicita a chave da API
        api_key = st.text_input(
            "Insira sua chave da API do Groq:",
            type="password"
        )

        idioma = st.text_input("Idioma de destino", "Digite o idioma desejado (ex: Inglês, Espanhol, Francês, Italiano...)")
        texto_usuario = st.text_area("Digite seu texto aqui")
        submit_tradutor = st.form_submit_button("Traduzir Texto")

        if submit_tradutor:
            if not api_key:
                st.error("Por favor, insira sua chave da API do Groq antes de traduzir.")
            elif not texto_usuario.strip():
                st.warning("Digite um texto para traduzir.")
            else:
                try:
                    # Inicializa o modelo ChatGroq
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

                    # Remove tudo entre <think> e </think>
                    resultado_limpo = re.sub(r"<think>.*?</think>", "", resultado, flags=re.DOTALL).strip()

                    st.write("### 🌍 Tradução:")
                    st.success(resultado_limpo)
                except Exception as e:
                    st.error(f"Erro: {e}")