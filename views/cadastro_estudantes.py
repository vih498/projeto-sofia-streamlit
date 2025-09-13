import streamlit as st
from controllers.estudante_controller import (
    adicionar_estudante,
    listar_estudante,
    atualizar_estudante,
    deletar_estudante,
)

# ---------- FUNÇÃO PRINCIPAL ----------
def show():

# ---------- ABAS ----------
    aba_adicionar, aba_listar_alterar_eliminar = st.tabs(
        ["Adicionar Estudante", "Listar, Alterar ou Excluir Estudante"]
    )

# ---------- ABA - adicionar ----------
    with aba_adicionar:
        st.subheader("Cadastro de Estudante")

# ---------- Formulário de cadastro ----------
        with st.form("cadastro_form"):
            nome = st.text_input("Nome")
            sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
            matricula = st.text_input("Matrícula")
            nota1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
            nota2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)
            submitted = st.form_submit_button("Cadastrar")

# ---------- Ação de submeter ----------
            if submitted:
                adicionar_estudante(nome, sexo, matricula if matricula else None, nota1, nota2)
                st.success("Estudante cadastrado com sucesso!")

# ---------- Lista simples de nomes ----------
        st.subheader("Lista de Alunos")
        estudantes = listar_estudante()
        if estudantes:
            for e in estudantes:
                st.write(f"👤 {e.nome}")
        else:
            st.info("Nenhum estudante cadastrado.")

# ---------- ABA - Listar, alterar ou excluir ----------
    with aba_listar_alterar_eliminar:
        st.subheader("Estudantes Cadastrados")

        estudantes = listar_estudante()
        if not estudantes:
            st.info("Nenhum estudante cadastrado.")
        else:
            for c in estudantes:

# ---------- Função EXPANDER por estudante ----------
                with st.expander(f"{c.nome} - Matrícula {c.matricula}"):

# ---------- Campos de edição ----------
                    novo_nome = st.text_input(
                        f"Nome - ID {c.matricula}", value=c.nome, key=f"nome{c.matricula}"
                    )
                    novo_sexo = st.selectbox(
                        "Sexo",
                        ["Masculino", "Feminino"],
                        index=["Masculino", "Feminino"].index(c.sexo),
                        key=f"sexo{c.matricula}"
                    )
                    nova_nota1 = st.number_input(
                        "Nota 1", min_value=0.0, max_value=10.0,
                        value=c.nota1 if c.nota1 else 0.0, step=0.1,
                        key=f"nota1{c.matricula}"
                    )
                    nova_nota2 = st.number_input(
                        "Nota 2", min_value=0.0, max_value=10.0,
                        value=c.nota2 if c.nota2 else 0.0, step=0.1,
                        key=f"nota2{c.matricula}"
                    )

# ---------- Botões de ação ----------
                    col1, col2 = st.columns(2)
                    if col1.button("Atualizar", key=f"update{c.matricula}"):
                        atualizar_estudante(c.matricula, novo_nome, novo_sexo, nova_nota1, nova_nota2)
                        st.success("Atualizado com sucesso!")

                    if col2.button("Excluir", key=f"delete{c.matricula}"):
                        deletar_estudante(c.matricula)
                        st.warning("Estudante excluído!")