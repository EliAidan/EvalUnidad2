from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyGenero(enum.Enum):
    Masculino ="Masculino"
    Femenino ="Femenino"

class Nacimientos(Base):
    __tablename__ = "tbb_nacimientos"
    
    ID = Column(Integer, primary_key=True, index=True)
    Padre = Column(String(255))
    Madre = Column(String(255))
    Signos_vitales = Column(String(255))
    Estatus = Column(Boolean, default=False)
    Calificacion_APGAR = Column(String(255))
    Observaciones = Column(String(255))
    Genero = Column(Enum(MyGenero))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    