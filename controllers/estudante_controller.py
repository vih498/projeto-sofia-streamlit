from models.estudantes_model import Estudante
import sqlite3
import os

# Banco unificado dentro da pasta data
DB_NAME = os.path.join("data", "database.sqlite")

# Conexão
def get_connection():
    return sqlite3.connect(DB_NAME)

# Inicializa banco e tabela
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudante (
            matricula INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sexo TEXT
        )
    """)
    conn.commit()
    conn.close()

# Conexão alternativa (mantida, mas aponta para mesmo banco)
def conectar():
    return sqlite3.connect(DB_NAME)

# ADICIONAR ESTUDANTE
def adicionar_estudante(nome, sexo, matricula=None):
    conn = get_connection()
    cursor = conn.cursor()
    if matricula:
        cursor.execute(
            "INSERT INTO estudante (nome, sexo, matricula) VALUES (?, ?, ?)",
            (nome, sexo, matricula)
        )
    else:
        cursor.execute(
            "INSERT INTO estudante (nome, sexo) VALUES (?, ?)",
            (nome, sexo)
        )
    conn.commit()
    conn.close()

# LISTAR ESTUDANTE
def listar_estudante():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT matricula, nome, sexo FROM estudante")
    rows = cursor.fetchall()
    conn.close()
    return [Estudante(*row) for row in rows]

# ATUALIZAR ESTUDANTE
def atualizar_estudante(matricula, nome, sexo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE estudante SET nome=?, sexo=? WHERE matricula=?
    """, (nome, sexo, matricula))
    conexao.commit()
    conexao.close()

# DELETAR ESTUDANTE
def deletar_estudante(matricula):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM estudante WHERE matricula=?", (matricula,))
    conexao.commit()
    conexao.close()
