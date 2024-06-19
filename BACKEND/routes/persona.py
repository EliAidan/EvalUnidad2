from fastapi import ApiRouter

persona = ApiRouter()

@persona.get("/personas")

def helloworld():
    return "Hello Word"