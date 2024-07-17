from fastapi import FastAPI
from routes.users import user
from routes.person import person
from routes.rol import rol
from routes.usersrols import userrol

app=FastAPI(
    title="Hospital Privilage Care",
    description="API para el almacenamiento de informacipn de un hospital"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
print ("Hola bienvenido a mi backend")