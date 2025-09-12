import streamlit as st
from controllers.estudante_controller import init_db

# ---------- INICIALIZAÇÃO DO BANCO ----------
init_db()  # garante que a tabela 'estudante' exista antes de qualquer consulta

# ---------- TÍTULO PRINCIPAL ----------
st.markdown(
    '<h1 style="color:black; font-size:75px;">Projeto SofIA - 498</h1>', 
    unsafe_allow_html=True
)

# ---------- IMPORTAÇÃO DAS ABAS DEPOIS DO TÍTULO ----------
from views import analise_documentos, cadastro_estudantes, conteudo_ia, dashboard_escolar, tradutor

# ---------- MENU DE NAVEGAÇÃO ----------
st.sidebar.title("Menu")
opcao = st.sidebar.radio(
    "Categorias", 
    ["Cadastro de Aluno", "Dashboard Escolar", "Análise de Documentos", "Conteúdo com IA", "Tradutor"]
)

if opcao == "Cadastro de Aluno":
    cadastro_estudantes.show()
elif opcao == "Dashboard Escolar":
    dashboard_escolar.show()
elif opcao == "Análise de Documentos":
    analise_documentos.show()
elif opcao == "Conteúdo com IA":
    conteudo_ia.show()
elif opcao == "Tradutor":
    tradutor.show()

# ---------- DESIGN ----------
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
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)