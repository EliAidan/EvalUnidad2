from fastapi import FastAPI
from routes.persona import persona
from routes.usuarios import usuarios

app = FastAPI()
app.include_router(persona)
app.include_router(usuarios)


print("Bienvenido a mi aplicacion")