from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.roles,config.db,schemas.roles,models.roles
from typing import List

roles = APIRouter()

models.roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@roles.get("/roles/", response_model=List[schemas.roles.Rol], tags=["roles"] ,dependencies=[Depends(Portador())])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_roles= crud.roles.get_rols(db=db, skip=skip, limit=limit)
    return db_roles

@roles.post("/rol/{ID}", response_model=schemas.roles.Rol, tags=["roles"] ,dependencies=[Depends(Portador())])
def read_rol(ID: int, db: Session = Depends(get_db)):
    db_rol= crud.roles.get_rol(db=db, ID=ID)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="rol not found")
    return db_rol

@roles.post("/roles/", response_model=schemas.roles.Rol, tags=["roles"])
def create_rol(rol: schemas.roles.RolCreate, db: Session = Depends(get_db)):
    db_rol = crud.roles.get_rol_by_nombre(db, nombre=rol.nombre)
    if db_rol:
        raise HTTPException(status_code=400, detail="rol existente intenta nuevamente")
    return crud.roles.create_rols(db=db, roles=rol)

@roles.put("/rol/{ID}", response_model=schemas.roles.Rol, tags=["roles"] ,dependencies=[Depends(Portador())])
def update_rol(ID: int, rol: schemas.roles.RolUpdate, db: Session = Depends(get_db)):
    db_rol = crud.roles.update_rol(db = db, ID = ID, roles = rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="rol no existente, no esta actuaizado")
    return db_rol

@roles.delete("/rol/{ID}", response_model=schemas.roles.Rol, tags=["roles"] ,dependencies=[Depends(Portador())])
def delete_rol(ID: int, db: Session = Depends(get_db)):
    db_rol = crud.roles.delete_rol(db = db, ID = ID)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="rol no existe, no se pudo eliminar")
    return db_rol