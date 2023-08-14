from pydantic import BaseModel
from typing import Optional

class EtlComplex(BaseModel):
    id_cia: str
    fdesde: Optional[str] = None
    fhasta: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "id_cia": "66",
                "fdesde": "01/01/20",
                "fhasta": "01/01/24"
            }]
        }
    }

class EtlBasic(BaseModel):
    id_cia: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [{
                    "id_cia": "66"
                }]
        }
    }