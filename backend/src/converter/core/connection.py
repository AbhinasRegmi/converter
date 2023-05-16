import motor.motor_asyncio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

from converter.core.config import settings

engine = create_engine(
    url=settings.POSTGRES_CONN_URI
)


class Base(DeclarativeBase):
    pass


session_local_postgres = sessionmaker(autocommit=False, autoflush=False, bind=engine)
client_local_mongo = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_CONN_URI)
