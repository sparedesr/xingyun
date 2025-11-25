from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
from app.database import crear_tabla, inicializar_galletas, obtener_galletas, cursor, conn

app = FastAPI(title="Galletas de la Fortuna")

# Inicializar base de datos al arrancar
@app.on_event("startup")
def startup():
    crear_tabla()
    inicializar_galletas()

# Modelo para POST
class Galleta(BaseModel):
    frase: str

@app.post("/agregar_galleta")
def agregar_galleta(galleta: Galleta):
    cursor.execute("INSERT INTO galletas (frase) VALUES (?)", (galleta.frase,))
    conn.commit()
    return {"mensaje": "¡Galleta agregada correctamente!"}

@app.get("/consultar_galleta")
def consultar_galleta():
    todas = obtener_galletas()
    if not todas:
        raise HTTPException(status_code=404, detail="No hay galletas disponibles")
    seleccionada = random.choice(todas)
    return {"galleta": seleccionada}
