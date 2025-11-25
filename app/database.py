import sqlite3

# Crear o conectar a la base de datos
conn = sqlite3.connect("galletas.db", check_same_thread=False)
cursor = conn.cursor()

# Crear tabla de galletas si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS galletas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    frase TEXT NOT NULL
)
""")
conn.commit()

# Insertar 2-3 frases predefinidas si la tabla está vacía
cursor.execute("SELECT COUNT(*) FROM galletas")
if cursor.fetchone()[0] == 0:
    frases_iniciales = [
        "La paciencia es una virtud.",
        "Hoy es un buen día para sonreír.",
        "Confía en tu intuición."
    ]
    cursor.executemany("INSERT INTO galletas (frase) VALUES (?)", [(f,) for f in frases_iniciales])
    conn.commit()
