from sqlalchemy import create_engine, text
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_mysql,
)