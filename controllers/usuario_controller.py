import sqlite3
import hashlib
import os

# Caminho do banco de dados
DB_PATH = os.path.join("data", "database.sqlite")

def criar_tabela_usuarios():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def adicionar_usuario(username: str, password: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        senha_hash = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute(
            "INSERT INTO usuarios (username, password) VALUES (?, ?)",
            (username, senha_hash)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Usuário já existe
    conn.close()
    return True

def validar_usuario(username: str, password: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    senha_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute(
        "SELECT * FROM usuarios WHERE username = ? AND password = ?",
        (username, senha_hash)
    )
    user = cursor.fetchone()
    conn.close()
    return user is not None