from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir acceso desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos de ejemplo para la tabla de posiciones
data = [
    {"posicion": 1, "usuario": "Juan", "mensajes": 125},
    {"posicion": 2, "usuario": "María", "mensajes": 110},
    {"posicion": 3, "usuario": "Pedro", "mensajes": 95},
    {"posicion": 4, "usuario": "Ana", "mensajes": 87},
]

@app.get("/posiciones")
def obtener_posiciones():
    return {"posiciones": data}
