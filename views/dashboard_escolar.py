import streamlit as st
import pandas as pd
import plotly.express as px
from controllers.estudante_controller import listar_estudante

def show():
    st.title("Dashboard Escolar")

    estudantes = listar_estudante()

    if not estudantes:
        st.info("Nenhum estudante cadastrado ainda.")
        return

    df = pd.DataFrame([{
        "Matrícula": e.matricula,
        "Nome": e.nome,
        "Sexo": e.sexo,
        "Nota 1": e.nota1,
        "Nota 2": e.nota2,
        "Média": e.media,
        "Status": e.status
    } for e in estudantes])

    st.subheader("Dados dos Estudantes")
    st.dataframe(df, use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)

    sexo_count = df["Sexo"].value_counts().reset_index()
    sexo_count.columns = ["Sexo", "Quantidade"]
    fig_sexo = px.bar(
        sexo_count,
        x="Sexo",
        y="Quantidade",
        color="Sexo",
        text="Quantidade",
        color_discrete_sequence=["#800080", "#9370DB"]
    )
    col1.subheader("Distribuição por Sexo")
    col1.plotly_chart(fig_sexo, use_container_width=True)

    status_count = df["Status"].value_counts().reset_index()
    status_count.columns = ["Status", "Quantidade"]
    fig_status = px.pie(
        status_count,
        names="Status",
        values="Quantidade",
        color="Status",
        color_discrete_map={
            "Aprovado": "#77dd77",
            "Recuperação": "#ffc067",
            "Reprovado": "#ff746c"
        }
    )
    col2.subheader("Situação dos Estudantes")
    col2.plotly_chart(fig_status, use_container_width=True)