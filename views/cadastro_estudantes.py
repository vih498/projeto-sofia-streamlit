import streamlit as st
from controllers.estudante_controller import adicionar_estudante, listar_estudante, atualizar_estudante, deletar_estudante

# ---------- FUNÇÃO PRINCIPAL ----------
def show():

    # ---------- ABAS ----------
    aba_adicionar, aba_listar_alterar_eliminar = st.tabs(["Adicionar Estudante", "Listar, Alterar ou Excluir Estudante"])

    # ---------- ABA - ADICIONAR ----------
    with aba_adicionar:
        st.subheader("Cadastro de Estudante")

        with st.form("cadastro_form"):
            nome = st.text_input("Nome")
            sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
            matricula = st.text_input("Matrícula")
            submitted = st.form_submit_button("Cadastrar")

            if submitted:
                adicionar_estudante(nome, sexo, matricula)
                st.success("Estudante cadastrado com sucesso!")

        st.subheader("Lista de Estudantes")
        estudantes = listar_estudante()
        if not estudantes:
            st.info("Nenhum estudante cadastrado.")
        else:
            for e in estudantes:
                st.write(f"👤 {e.nome}")

    # ---------- ABA - LISTAR, ALTERAR OU EXCLUIR ----------
    with aba_listar_alterar_eliminar:
        st.subheader("Estudantes Cadastrados")

        # Função para atualizar a lista de estudantes após ações
        def atualizar_lista():
            return listar_estudante()

        estudantes = atualizar_lista()
        if not estudantes:
            st.info("Nenhum estudante cadastrado.")
        else:
            for c in estudantes:
                with st.expander(f"{c.nome} - {c.matricula}"):
                    novo_nome = st.text_input(f"Nome - ID {c.matricula}", value=c.nome, key=f"nome{c.matricula}")
                    novo_sexo = st.selectbox(
                        "Sexo",
                        ["Masculino", "Feminino"],
                        index=["Masculino", "Feminino"].index(c.sexo),
                        key=f"sexo{c.matricula}"
                    )
                    nova_matricula = st.text_input("Matrícula", value=c.matricula, key=f"matricula{c.matricula}")

                    col1, col2 = st.columns(2)
                    if col1.button("Atualizar", key=f"update{c.matricula}"):
                        atualizar_estudante(c.matricula, novo_nome, novo_sexo)
                        st.success("Atualizado com sucesso!")
                        estudantes = atualizar_lista()  # recarrega os dados

                    if col2.button("Excluir", key=f"delete{c.matricula}"):
                        deletar_estudante(c.matricula)
                        st.warning("Estudante excluído!")
                        estudantes = atualizar_lista()  # recarrega os dados