import streamlit as st
from controllers.estudante_controller import init_db, atualizar_tabela
from views import login, cadastro_estudantes, dashboard_escolar
from views import conteudo_ia, tradutor, analise_documentos

init_db()
atualizar_tabela()

st.markdown('<h1 style="color:black; font-size:75px;">Projeto SofIA - 498</h1>', unsafe_allow_html=True)

if "api_key" not in st.session_state:
    st.session_state.api_key = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login.login()
    st.stop()

st.sidebar.title("Menu")
opcao = st.sidebar.radio(
    "Categorias",
    ["Cadastro de Aluno", "Dashboard Escolar", "IA com Groq"]
)

if opcao == "Cadastro de Aluno":
    cadastro_estudantes.show()
elif opcao == "Dashboard Escolar":
    dashboard_escolar.show()
elif opcao == "IA com Groq":
    # ---------- Abas horizontais ----------
    abas = st.tabs(["Geração de Conteúdo", "Tradutor", "Análise de Documentos"])
    
    with abas[0]:
        conteudo_ia.show()
    
    with abas[1]:
        tradutor.show()
    
    with abas[2]:
        analise_documentos.show()

page_bg = """
<style>
    /* Fundo */
    .stApp {
        background-color: #EADCF8;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F0EAF5;
        color: white;
    }
    
    /* Título h1 (principal) */
    h1 {
        color: #6A329F;
    }

    /* Títulos h2, h3 (subtítulos) */
    h2, h3 {
        color: #6A0DAD;
    }

    /* Texto padrão */
    .stApp, .stApp p, .stApp div, .stApp span {
        color: #6A329F;
    }

    /* Inputs e botões */
    .stTextInput>div>div>input {
        background-color: #F0EAF5;
        color: #6A329F;
    }
    div.stButton>button {
        background-color: #6A329F !important;
        color: #FFFFFF !important;
        font-weight: bold;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)