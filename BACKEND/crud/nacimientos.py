import models.nacimientos
import schemas.nacimientos
from sqlalchemy.orm import Session

def get_nacimiento(db: Session, ID: int):
    return db.query(models.nacimientos.Nacimientos).filter(models.nacimientos.Nacimientos.ID == ID).first()

def get_nacimientos_by_padre(db: Session, Padre: str):
    return db.query(models.nacimientos.Nacimientos).filter(models.nacimientos.Nacimientos.Padre == Padre).all()

def get_nacimientos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.nacimientos.Nacimientos).offset(skip).limit(limit).all()

def create_nacimiento(db: Session, nacimiento: schemas.nacimientos.NacimientosCreate):
    db_nacimiento = models.nacimientos.Nacimientos(
        Padre=nacimiento.Padre,
        Madre=nacimiento.Madre,
        Signos_vitales=nacimiento.Signos_vitales,
        Estatus=nacimiento.Estatus,
        Calificacion_APGAR=nacimiento.Calificacion_APGAR,
        Observaciones=nacimiento.Observaciones,
        Genero=nacimiento.Genero,
        Fecha_Registro=nacimiento.Fecha_Registro,
        Fecha_Actualizacion=nacimiento.Fecha_Actualizacion
    )
    db.add(db_nacimiento)
    db.commit()
    db.refresh(db_nacimiento)
    return db_nacimiento

def update_nacimiento(db: Session, ID: int, nacimiento: schemas.nacimientos.NacimientosUpdate):
    db_nacimiento = db.query(models.nacimientos.Nacimientos).filter(models.nacimientos.Nacimientos.ID == ID).first()
    if db_nacimiento:
        for var, value in vars(nacimiento).items():
            setattr(db_nacimiento, var, value) if value else None
        db.commit()
        db.refresh(db_nacimiento)
    return db_nacimiento

def delete_nacimiento(db: Session, ID: int):
    db_nacimiento = db.query(models.nacimientos.Nacimientos).filter(models.nacimientos.Nacimientos.ID == ID).first()
    if db_nacimiento:
        db.delete(db_nacimiento)
        db.commit()
    return db_nacimiento
