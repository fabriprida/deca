from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitar CORS para que el frontend pueda comunicarse con el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto a la URL de tu frontend en producción
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido al backend con FastAPI!"}
