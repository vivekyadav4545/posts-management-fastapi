from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 


import time
## this part is for using sql command
import  psycopg2  
from psycopg2.extras import RealDictCursor 

from .config import settings


SQL_ALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False,autoflush= False,bind= engine)

Base = declarative_base()


## dependency 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally :
        db.close()

## data base connection

# while True :
#     try:
#         conn = psycopg2.connect(host='localhost' , database='fastapidb',
#         user='postgres',password= '221711')
#         cursor = conn.cursor(cursor_factory=RealDictCursor)
#         print("Database connection is successfully!")
#         break
#     except Exception as error:
#         print("connecting to database failed")
#         print("Error:",error)
#         time.sleep(2)
