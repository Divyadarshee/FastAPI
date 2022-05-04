from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
Changes from sqlite3 to PostgreSQL
1. change in database url
2. engine parameters (connect_args) was specific to sqlite3 only
'''

# sqlite3
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:dvd6900@localhost/TodoApplicationDatabase"

# MySQL
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:dvd6900@127.0.0.1:3306/todoapp"  # mysql+mysql://{username}:
                                                                                 # {password}@{url_for_database}:
                                                                                 # {port_for_database}/{database_name}

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