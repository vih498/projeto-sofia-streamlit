import streamlit as st

def login():
    """Exibe a tela de login e guarda a chave no session_state"""
    st.subheader("Login com API Groq")

    api_key = st.text_input("Digite sua chave da API Groq:", type="password")

    if st.button("Entrar"):
        if api_key and api_key.startswith("gsk_"):
            st.session_state.api_key = api_key
            st.session_state.logged_in = True
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("Chave inválida. Verifique e tente novamente.")

def check_login():
    """Protege páginas que precisam da API Key"""
    if "api_key" not in st.session_state or not st.session_state.api_key:
        st.error("⚠️ Você precisa inserir sua chave da API Groq na tela de login.")
        st.stop()

st.markdown(
    """
    <style>
        /* Fundo da aplicação */
        .stApp {
            background-color: #EADCF8;
        }

        /* Caixa do input e botão */
        .stTextInput>div>div>input {
            background-color: #F0EAF5;
            color: #6A329F;
        }

        /* Botão */
        div.stButton>button {
            background-color: #F0EAF5;
            color: white;
        }

        /* Subtítulo */
        h2, h3, h1, p, div, span {
            color: #6A329F;
        }
    </style>
    """,
    unsafe_allow_html=True
)