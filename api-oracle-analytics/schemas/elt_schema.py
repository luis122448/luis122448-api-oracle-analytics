from pydantic import BaseModel
from typing import Optional

class EtlComplex(BaseModel):
    id_cia: str
    pin_fdesde: Optional[str] = None
    pin_fhasta: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "id_cia": "66",
                "pin_fdesde": "2023-01-01",
                "pin_fhasta": "2024-01-01"
            }]
        }
    }

class EtlBasic(BaseModel):
    id_cia: str
    
    model_config = {
     "json_schema_extra": {
            "examples": [
                {
                    "id_cia": "66"
                }
            ]
        }
    }