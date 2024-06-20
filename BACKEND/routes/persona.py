from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

persona = APIRouter()
personas=[]

class listar_personas(BaseModel):
    id: str
    nombre: str
    primer_apellido: str
    segundo_apellido: Optional[str]
    edad: int
    fecha_nacimiento: datetime
    curp: str
    tipo_sangre: str
    created_at: datetime = datetime.now()
    estatus: bool = False

@persona.get('/')

def bienvenida():
    return "Bienvenido al sistema de API"

@persona.get("/personas")

def get_personas():
    return personas

@persona.post('/personas')
def save_personas(datos_persona:listar_personas):
    personas.append(datos_persona)
    return "Datos guardados correctamente"