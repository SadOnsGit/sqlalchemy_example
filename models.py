from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()

# Императивный стиль написания моделей
workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String(length=20), nullable=False),
)

