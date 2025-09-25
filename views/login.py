import streamlit as st
from controllers.usuario_controller import (
    criar_tabela_usuarios,
    adicionar_usuario,
    validar_usuario
)

def login():
    criar_tabela_usuarios()

    st.subheader("Login")

    tab_login, tab_registro = st.tabs(["Entrar", "Cadastre-se"])

    with tab_login:
        username = st.text_input("Usuário:")
        password = st.text_input("Senha:", type="password")
        api_key = st.text_input("Digite sua chave da API Groq:", type="password")

        if st.button("Entrar"):
            if validar_usuario(username, password):
                if api_key and api_key.startswith("gsk_"):
                    st.session_state.username = username
                    st.session_state.api_key = api_key
                    st.session_state.logged_in = True
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("Chave da API inválida. Verifique e tente novamente.")
            else:
                st.error("Usuário ou senha incorretos.")

    with tab_registro:
        new_username = st.text_input("Novo usuário:")
        new_password = st.text_input("Nova senha:", type="password")

        if st.button("Registrar"):
            if new_username.strip() == "" or new_password.strip() == "":
                st.warning("Preencha todos os campos para registrar.")
            else:
                if adicionar_usuario(new_username, new_password):
                    st.success("Usuário registrado com sucesso! Agora você pode fazer login.")
                else:
                    st.error("Nome de usuário já existe. Tente outro.")

def check_login():
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.error("Você precisa fazer login primeiro.")
        st.stop()

st.markdown(
    """
    <style>
        /* Fundo da aplicação */
        .stApp {
            background-color: #EADCF8;
        }

        /* Inputs */
        .stTextInput>div>div>input {
            background-color: #F0EAF5;
            color: #6A329F;
        }

        /* Botão */
        div.stButton>button {
            background-color: #FFFFFF;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1em;
        }

        /* Subtítulos e textos */
        h1, h2, h3, p, div, span, label {
            color: #6A329F !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)