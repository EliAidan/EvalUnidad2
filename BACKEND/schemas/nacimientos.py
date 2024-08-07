from typing import List,Union
from pydantic import BaseModel
from datetime import datetime
from models.persons import MyGenero

class NacimientoBase(BaseModel):
    
    Padre:str
    Madre: str
    Signos_vitales: str
    Estatus: str
    Calificacion_APGAR:  int  
    Observaciones: str
    Genero: MyGenero
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime


    
    
class NacimientosCreate(NacimientoBase):
    pass
class NacimientosUpdate(NacimientoBase):
    pass
class Nacimientos(NacimientoBase):
    ID: int

    class Config:
        orm_mode = True