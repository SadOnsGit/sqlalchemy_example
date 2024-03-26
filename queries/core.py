from sqlalchemy import Text
from database import engine
from models import metadata_obj


def create_tables():
    metadata_obj.create_all(engine)