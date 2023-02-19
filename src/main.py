from fastapi import FastAPI
from .routers import CRouterModels

app = FastAPI()

app.include_router(CRouterModels.router)


@app.get("/test")
def read_root():
    return 1


