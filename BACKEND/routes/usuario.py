# from fastapi import APIRouter
# from pydantic import BaseModel
# from datetime import datetime


# usuario = APIRouter()
# usuarios = []

# class model_usuarios(BaseModel):
#     id:int
#     usuario:str
#     contrasena:str
#     persona_id:int
#     created_at:datetime = datetime.now()
#     estatus:bool = False



# @usuario.get("/usuarios")
# def get_usuarios():
#     return usuarios

# @usuario.post("/usuarios")
# def saveUsuarios(datos_usuario:model_usuarios):
#     usuarios.append(datos_usuario)
#     return "Datos guardados correctamente"


# @usuario.get("/usuarios/{usuario_id}")
# def get_usuarios(usuario_id: int):
#     for usuario in usuarios:
#         if usuario.id == usuario_id:
#             return usuario
        
# @usuario.put("/usuarios/{usuario_id}")
# def update_usuarios(usuario_id: int, datos_usuario: model_usuarios):
#     for index, usuario in enumerate(usuarios):
#         if usuario.id == usuario_id:
#             # Evitar actualizar el campo 'id'
#             datos_usuario.id = usuario.id  # Mantener el mismo id
#             usuarios[index] = datos_usuario
#             return "Datos actualizados correctamente"



# @usuario.delete("/usuarios/{usuario_id}")
# def delete_usuarios(usuario_id: int):
#     for index, usuario in enumerate(usuarios):
#         if usuario.id == usuario_id:
#             del usuarios[index]
#             return "Persona eliminada correctamente"
