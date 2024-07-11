from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    descripcion = Column(LONGTEXT)
    estatus = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    #items = relationship("Item", back_populates="owner") Clave Foranea