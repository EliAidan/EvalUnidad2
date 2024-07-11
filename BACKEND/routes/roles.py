from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
import crud.users, config.db, schemas.users, models.users
from typing import List

rol = APIRouter()

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@user.get("/roles/", response_model=List[schemas.roles.Rol], tags=["Roles"])
def read_rol(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_rol= crud.rol.get_rol(db=db, skip=skip, limit=limit)
    return db_rol

@user.post("/roles/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def read_rol(id: int, db: Session = Depends(get_db)):
    db_rol= crud.rol.get_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_rol

@user.post("/roles/", response_model=schemas.roles.Rol, tags=["Roles"])
def create_rol(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_rol = crud.rol.get_rol_by_roles(db, rol=rol.roles)
    if db_rol:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.rol.create_rol(db=db, rol=rol)

@user.put("/roles/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def update_rol(id: int, user: schemas.roles.RolUpdate, db: Session = Depends(get_db)):
    db_rol = crud.rol.update_rol(db=db, id=id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_rol

@user.delete("/roles/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def delete_rol(id: int, db: Session = Depends(get_db)):
    db_rol = crud.rol.delete_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_rol