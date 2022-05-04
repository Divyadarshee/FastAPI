from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

'''
Changes from sqlite3 to PostgreSQL
1. change in database url
2. engine parameters (connect_args) was specific to sqlite3 only
'''

# sqlite3
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# PostgreSQL
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:dvd6900@localhost/TodoApplicationDatabase"

# MySQL
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:dvd6900@127.0.0.1:3306/todoapp"  # mysql+mysql://{username}:
                                                                                 # {password}@{url_for_database}:
                                                                                 # {port_for_database}/{database_name}

#Heroku Postgres
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
# Below replacement is required because postgres url from heroku doesnt contain ql which is neede to connectgit
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)


# sqlite3
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

#PostgreSQL and MySQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()