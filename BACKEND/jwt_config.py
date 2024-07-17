from jwt import encode,decode

def solicita_token(dato:dict)->str:
    token:str=encode(payload=dato,key='mi_clave',algorithm='HS256')
    return token

def valida_token(token:str)->dict:
    dato:str=decode(token,key='mi_clave',algorithm=['HS256'])
    return dato
