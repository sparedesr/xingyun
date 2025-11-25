from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
from app.database import cursor, conn

app = FastAPI(title="Galletas de la Fortuna")

# Modelo para recibir la galleta en POST
class Galleta(BaseModel):
    frase: str

@app.post("/agregar_galleta")
def agregar_galleta(galleta: Galleta):
    cursor.execute("INSERT INTO galletas (frase) VALUES (?)", (galleta.frase,))
    conn.commit()
    return {"mensaje": "¡Galleta agregada correctamente!"}

@app.get("/consultar_galleta")
def consultar_galleta():
    cursor.execute("SELECT frase FROM galletas")
    todas = cursor.fetchall()
    if not todas:
        raise HTTPException(status_code=404, detail="No hay galletas disponibles")
    seleccionada = random.choice(todas)[0]
    return {"galleta": seleccionada}
