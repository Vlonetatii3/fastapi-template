#Core
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

#Schemas
from schemas.responseModel import HealthResponse
from schemas.DatabaseResponse import DbResponse
#database
from db.oracle import get_oracle_db

router = APIRouter(
    tags=["Application Started"]
)

@router.get("/health",
            summary="Check the application health", 
            response_model=HealthResponse)
def check_health():
    return {"message": "Aplication running"}


@router.get("/health/db",
            summary="Check the connection with the database...", 
            response_model=DbResponse)
def check_health(db: Session = Depends(get_oracle_db)):
    return {"status": "ok"}