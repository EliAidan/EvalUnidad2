from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    nombre: str
    descripcion: str
    estatus: bool
    created_at: datetime
    updated_at: datetime

class RolCreate(UserBase):
    pass

class RolUpdate(UserBase):
    pass

class Rol(UserBase):
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True