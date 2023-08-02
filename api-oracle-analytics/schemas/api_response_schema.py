from pydantic import BaseModel
from typing import Optional

class ApiResponseSchema(BaseModel):
    status: int
    message: str
    id_cia: Optional[str] = None
    timestamp: Optional[str] = None