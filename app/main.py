from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .kubestart import start

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# 쿠버네티스 kubestart
@app.get("/signal")
def kubestart():
    path = start()
    return path
start()