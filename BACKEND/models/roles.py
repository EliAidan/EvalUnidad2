from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    __tablename__ = "tbc_roles"
    
    ID = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    descripcion = Column(String(255))
    estatus = Column(Boolean, default=False)
    created_at = Column(DateTime)
    fecha_actualizacion = Column(DateTime)

