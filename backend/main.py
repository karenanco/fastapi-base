from fastapi import FastAPI
from db import conectar_db

app = FastAPI()

@app.get("/listo")
def home():
    return {"status": "ok", "mensaje": "API funcionando 🚀"}

@app.get("/buscar_noticias")
def obtener_noticias(query : str):
    noticias = buscar_noticias(query)
    


