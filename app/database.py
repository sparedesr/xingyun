import os
import sqlite3

# Ruta absoluta dentro de la carpeta app
DB_PATH = os.path.join(os.path.dirname(__file__), "galletas.db")

# Conexión y cursor
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# Función para crear la tabla si no existe
def crear_tabla():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS galletas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        frase TEXT NOT NULL
    )
    """)
    conn.commit()

# Función para insertar galletas iniciales si la tabla está vacía
def inicializar_galletas():
    cursor.execute("SELECT COUNT(*) FROM galletas")
    total = cursor.fetchone()[0]
    if total == 0:
        frases = [
            "No dejes que lo que no puedes controlar te controle.",
            "La paciencia es una virtud.",
            "Evita tomar jugo de naranja después de lavarte los dientes."
        ]
        for frase in frases:
            cursor.execute("INSERT INTO galletas (frase) VALUES (?)", (frase,))
        conn.commit()

# Función para obtener todas las galletas
def obtener_galletas():
    cursor.execute("SELECT frase FROM galletas")
    return [fila[0] for fila in cursor.fetchall()]
