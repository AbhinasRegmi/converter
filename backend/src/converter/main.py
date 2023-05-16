from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from converter.api.router import router_v1
from converter.core.config import settings
from converter.dependencies.db_dep import MongoDbCollection

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    MongoDbCollection.close()


app = FastAPI(
    redoc_url='',
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.get("/", tags=["Home"])
def welcome():
    return {
        "message": "Welcome to Video-to-Audio-Converter"
    }


app.include_router(router_v1)