from fastapi import FastAPI
from routes.persona import persona

app = FastAPI()
app.include_router(persona)

print("Bienvenido a mi aplicacion")