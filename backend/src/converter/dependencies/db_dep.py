from sqlalchemy.orm import Session

from converter.core.config import settings
from converter.core.connection import client_local_mongo
from converter.core.connection import session_local_postgres

def get_postgres_db():
    """
    Gives a session of the database which can
    be used to access the database.
    """
    db = session_local_postgres()
    try:
        yield db
    finally:
        db.close()


class  MongoDbCollection:
    def __init__(self, collection_name: str) -> None:
        self._collection_name = collection_name
        self._db = client_local_mongo[settings.MONGODB_DB_NAME]

    def __call__(self):
        return self._db[self._collection_name]
    
    @classmethod
    def close(cls) -> None:
        client_local_mongo.close()


get_video_db = MongoDbCollection("videos")
get_user_db = MongoDbCollection("users")
