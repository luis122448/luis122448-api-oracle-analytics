from pydantic import BaseModel

class UsuarioAuthConfig(BaseModel):
    ruc: str
    coduser: str
    clave: str

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "ruc": "20516612143",
                "coduser": "admin",
                "clave": "TFRWUTIwMjM="
            }]
        }
    }