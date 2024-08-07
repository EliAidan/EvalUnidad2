from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.nacimientos, config.db, schemas.nacimientos, models.nacimientos
from typing import List

nacimiento_router = APIRouter()

models.nacimientos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@nacimiento_router.get("/nacimientos/", response_model=List[schemas.nacimientos.Nacimientos], tags=["Nacimientos"], dependencies=[Depends(Portador())])
def read_nacimientos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.nacimientos.get_nacimientos(db=db, skip=skip, limit=limit)

@nacimiento_router.get("/nacimiento/{ID}", response_model=schemas.nacimientos.Nacimientos, tags=["Nacimientos"], dependencies=[Depends(Portador())])
def read_nacimiento(ID: int, db: Session = Depends(get_db)):
    db_nacimiento = crud.nacimientos.get_nacimiento(db=db, ID=ID)
    if db_nacimiento is None:
        raise HTTPException(status_code=404, detail="Registro de nacimiento no encontrado")
    return db_nacimiento

@nacimiento_router.post("/nacimientos/", response_model=schemas.nacimientos.Nacimientos, tags=["Nacimientos"])
def create_nacimiento(nacimiento: schemas.nacimientos.NacimientosCreate, db: Session = Depends(get_db)):
    return crud.nacimientos.create_nacimiento(db=db, nacimiento=nacimiento)

@nacimiento_router.put("/nacimiento/{ID}", response_model=schemas.nacimientos.Nacimientos, tags=["Nacimientos"], dependencies=[Depends(Portador())])
def update_nacimiento(ID: int, nacimiento: schemas.nacimientos.NacimientosUpdate, db: Session = Depends(get_db)):
    db_nacimiento = crud.nacimientos.update_nacimiento(db=db, ID=ID, nacimiento=nacimiento)
    if db_nacimiento is None:
        raise HTTPException(status_code=404, detail="Registro de nacimiento no encontrado")
    return db_nacimiento

@nacimiento_router.delete("/nacimiento/{ID}", response_model=schemas.nacimientos.Nacimientos, tags=["Nacimientos"], dependencies=[Depends(Portador())])
def delete_nacimiento(ID: int, db: Session = Depends(get_db)):
    db_nacimiento = crud.nacimientos.delete_nacimiento(db=db, ID=ID)
    if db_nacimiento is None:
        raise HTTPException(status_code=404, detail="Registro de nacimiento no encontrado")
    return db_nacimiento
