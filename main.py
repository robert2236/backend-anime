from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from routes.animes import anime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

print(config("FRONTEND_URL"))

origins = [
    config("FRONTEND_URL"),
]

@app.get("/")
def read_root():
    return {"mensaje": "Hola mundo"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(anime)