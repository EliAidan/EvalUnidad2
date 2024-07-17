from fastapi import FastAPI
from routes.users import user
from routes.persons import person
from routes.rol import rol
from routes.usersrol import userrol

app=FastAPI(
    title="Hospital",
    description="API para el almacenamiento de informacipn de un hospital"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
print ("Hola bienvenido a mi backend")