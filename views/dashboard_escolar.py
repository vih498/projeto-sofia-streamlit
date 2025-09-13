import streamlit as st
import pandas as pd
import plotly.express as px
from controllers.estudante_controller import listar_estudante

# ---------- FUNÇÃO PRINCIPAL ----------
def show():
    st.title("Dashboard Escolar")

# ---------- Buscar dados ----------
    estudantes = listar_estudante()

    if not estudantes:
        st.info("Nenhum estudante cadastrado ainda.")
        return

# ---------- Converter para DataFrame ----------
    df = pd.DataFrame([{
        "Matrícula": e.matricula,
        "Nome": e.nome,
        "Sexo": e.sexo,
        "Nota 1": e.nota1,
        "Nota 2": e.nota2,
        "Média": e.media,
        "Status": e.status
    } for e in estudantes])

# ---------- Exibir tabela ----------
    st.subheader("Dados dos Estudantes")
    st.dataframe(df, use_container_width=True)

    st.divider()

# ---------- GRÁFICO - Sexo ----------
    st.subheader("Distribuição por Sexo")
    sexo_count = df["Sexo"].value_counts().reset_index()
    sexo_count.columns = ["Sexo", "Quantidade"]

    fig_sexo = px.bar(
        sexo_count,
        x="Sexo",
        y="Quantidade",
        color="Sexo",
        text="Quantidade",
        color_discrete_sequence=["#800080", "#9370DB"]  # Roxos
    )
    st.plotly_chart(fig_sexo, use_container_width=True)

    st.divider()

# ---------- GRÁFICO - Status ----------
    st.subheader("Situação dos Estudantes")
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
    st.plotly_chart(fig_status, use_container_width=True)

    st.divider()

# ---------- GRÁFICO - Médias por aluno ----------
    st.subheader("Médias dos Alunos")
    fig_media = px.bar(
    df,
    x="Média",
    y="Nome",
    orientation="h",
    text="Média",
    color="Média",  #usa a própria média para definir a cor
    color_continuous_scale=["#ff746c", "#ffc067", "#77dd77"],  #vermelho → amarelo → verde
    range_color=[0, 10]  #garante que a escala vá de 0 a 10
    )
    st.plotly_chart(fig_media, use_container_width=True)