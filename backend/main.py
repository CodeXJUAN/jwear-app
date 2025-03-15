from fastapi import FastAPI
from .database import engine, Base
from .routes import user

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir las rutas del módulo user
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de FastAPI"}