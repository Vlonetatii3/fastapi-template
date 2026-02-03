#CORE
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#ROUTES
from api.init import router as InitRouter
#APP start
app = FastAPI(
    title="Fastapi template",
    description="An application template with fastapi")

#CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"]
)

#Expose routes
app.include_router(InitRouter)
