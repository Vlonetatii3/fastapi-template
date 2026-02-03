from pydantic import BaseModel

class DbResponse(BaseModel):
    status: str