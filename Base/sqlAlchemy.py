# https://docs.sqlalchemy.org/en/20/dialects/postgresql.html
# pip install SQLAlchemy
import uuid

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgresql://postgres:1@localhost/postgres'  # 'postgresql://username:password@localhost/mydatabase'
)

session = sessionmaker(bind=engine)
metadata = MetaData()
session = session

def create_table():
    users = Table('usersers', metadata,
                  Column('id', UUID, primary_key=True, default=uuid.uuid4()),
                  Column('name', VARCHAR),
                  Column('username', VARCHAR, unique=True, nullable=False))
    print('yaratildi')


create_table()