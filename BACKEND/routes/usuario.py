from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

usuario = APIRouter()
usuarios=[]

class model_usuarios(BaseModel):
    id:int
    usuario:str
    password:str
    id_persona: int
    estatus: bool = False
    created_at: datetime = datetime.now()
    
@usuario.get('/usuarios')

def getUsuarios():
    return usuarios

@usuario.get('/usuarios/{id_usuario}')
def get_usuario(id_usuario: int):
    global usuarios
    
    # Buscar la persona por su ID
    for usuario in usuarios:
        if usuario.id == id_usuario:
            return usuario

    return f"No existe algun usuario con ese id: {id_persona} "


@usuario.post('/usuarios')

def save_usuario(datos_usuario:model_usuarios):
    usuarios.append(datos_usuario)
    return "Datos guardados correctamente"

@usuario.delete('/usuarios/{id_usuario}')

def delete_usuario(id_usuario: int):
    global usuarios
    
    # Buscar la persona por su ID
    for i, usuario in enumerate(usuarios):
        if usuario.id == id_usuario:
            del usuarios[i]
            return f"Dato con ID {id_usuario} eliminado correctamente."
    return f"No existe algun usuario con ese id: {id_usuario} "

@usuario.put('/usuarios/{id_usuario}')
def update_usuario(id_usuario: int, datos_usuario: model_usuarios):
    global usuarios
    
    # Buscar la persona por su ID
    for usuario in usuarios:
        if usuario.id == id_usuario:
            # Actualizar los campos de la persona
            usuario.usuario = datos_usuario.usuario
            usuario.password = datos_usuario.password

            return f"Dato con ID {id_usuario} actualizado correctamente."
    return f"No existe algun usuario con ese id: {id_usuario} "