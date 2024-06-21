from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

usuarios = APIRouter()
usuarios_data = []

class Usuario(BaseModel):
    id: int
    usuario: str
    password: str
    fecha_creacion: datetime = datetime.now()
    id_persona: int
    created_at: datetime = datetime.now()
    estatus: bool = False


# Obtener todos los usuarios
@usuarios.get('/usuarios')
def getUsuarios():
    return usuarios_data

# Obtener un usuario por su ID
@usuarios.get('/usuarios/{usuario_id}')
def getUsuario(usuario_id: int):
    for usuario in usuarios_data:
        if usuario['id'] == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Guardar un nuevo usuario
@usuarios.post('/usuarios')
def save_usuario(usuario: Usuario):
    usuarios_data.append(usuario.dict())
    return "Usuario guardado correctamente"

# Actualizar datos de un usuario por su ID
@usuarios.put('/usuarios/{usuario_id}')
def updateUsuario(usuario_id: int, usuario: Usuario):
    for index, user in enumerate(usuarios_data):
        if user['id'] == usuario_id:
            usuarios_data[index] = usuario.dict()
            return "Usuario actualizado correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Eliminar un usuario por su ID
@usuarios.delete('/usuarios/{usuario_id}')
def deleteUsuario(usuario_id: int):
    for index, user in enumerate(usuarios_data):
        if user['id'] == usuario_id:
            del usuarios_data[index]
            return "Usuario eliminado correctamente"
    raise HTTPException(status_code=404, detail="Usuario no encontrado")