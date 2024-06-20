from fastapi import FastAPI
from app.routers.router import router_api
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/frontend/static"), name="static")
app.include_router(router_api)

if __name__ == '__main__':
    uvicorn.run("main:app", port=9000, log_level="info")