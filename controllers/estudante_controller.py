from models.estudantes_model import Estudante
import sqlite3
import os

# ---------- Definiçãoo do banco de dados ----------
DB_NAME = os.path.join("data", "database.sqlite")

# ---------- Conexão com o banco ----------
def get_connection():
    return sqlite3.connect(DB_NAME)

# ---------- Inicialização de banco e tabela ----------
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

# ---------- Atualização de tabela (novas colunas) ----------
def atualizar_tabela():
    conn = get_connection()
    cursor = conn.cursor()

    colunas = {
        "nota1": "REAL",
        "nota2": "REAL",
        "media": "REAL",
        "status": "TEXT"
    }

    for coluna, tipo in colunas.items():
        try:
            cursor.execute(f"ALTER TABLE estudante ADD COLUMN {coluna} {tipo}")
        except sqlite3.OperationalError:
            # ignora se a coluna já existe
            pass

    conn.commit()
    conn.close()

# ---------- Conexão alternativa ----------
def conectar():
    return sqlite3.connect(DB_NAME)

# ---------- Função para calcular média e status ----------
def calcular_media_status(nota1, nota2):
    if nota1 is None: nota1 = 0
    if nota2 is None: nota2 = 0
    media = (nota1 + nota2) / 2
    if media >= 7:
        status = "Aprovado"
    elif media >= 5:
        status = "Recuperação"
    else:
        status = "Reprovado"
    return media, status

# ---------- ADICIONAR ESTUDANTE ----------
def adicionar_estudante(nome, sexo, matricula=None, nota1=None, nota2=None):
    media, status = calcular_media_status(nota1 or 0, nota2 or 0)
    conn = get_connection()
    cursor = conn.cursor()

    if matricula:
        cursor.execute(
            "INSERT INTO estudante (matricula, nome, sexo, nota1, nota2, media, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (matricula, nome, sexo, nota1, nota2, media, status)
        )
    else:
        cursor.execute(
            "INSERT INTO estudante (nome, sexo, nota1, nota2, media, status) VALUES (?, ?, ?, ?, ?, ?)",
            (nome, sexo, nota1, nota2, media, status)
        )
    conn.commit()
    conn.close()

# ---------- LISTAR ESTUDANTE ----------
def listar_estudante():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT matricula, nome, sexo, nota1, nota2, media, status FROM estudante")
    rows = cursor.fetchall()
    conn.close()
    return [Estudante(*row) for row in rows]

# ---------- ATUALIZAR ESTUDANTE ----------
def atualizar_estudante(matricula, nome, sexo, nota1, nota2):
    media, status = calcular_media_status(nota1, nota2)
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE estudante 
        SET nome=?, sexo=?, nota1=?, nota2=?, media=?, status=?
        WHERE matricula=?
    """, (nome, sexo, nota1, nota2, media, status, matricula))
    conexao.commit()
    conexao.close()

# ---------- DELETAR ESTUDANTE ----------
def deletar_estudante(matricula):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM estudante WHERE matricula=?", (matricula,))
    conexao.commit()
    conexao.close()