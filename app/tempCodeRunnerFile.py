from fastapi import FastAPI ,Body , Response,status,HTTPException,Depends # type: ignore
from pydantic import BaseModel # type: ignore
from typing import Optional,List
import time
from passlib.context import CryptContext
from random import randrange
from .database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from . import model,schemas
import  psycopg2  # type: ignore ## for connecting postgress database
from psycopg2.extras import RealDictCursor  # type: ignore ## it is used to connect only specific postgress database


## this is for password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

model.Base.metadata.create_all(bind=engine)



app = FastAPI()


## data base connection

while True :
    try:
        conn = psycopg2.connect(host='localhost' , database='fastapidb',
        user='postgres',password= '221711')
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        print("Database connection is successfully!")
        break
    except Exception as error:
        print("connecting to database failed")
        print("Error:",error)
        time.sleep(2)


my_posts = [{"title": "title of post 1","content ":"content of post 1","id": 1},{"title":"fav food","content":"i like pizza","id":2}]


def find_post(id):
    for p in my_posts :
        if p["id"] == id:
            return p



def find_index_post(id):
    for i ,p in enumerate(my_posts):
      if p['id'] == id :
          return i
        

@app.get("/posts")    # decorator
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()


    post = db.query(model.Post).all()
    return post


## for creating post

@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(post : schemas.PostCreate,db: Session = Depends(get_db)): 

    # cursor.execute(""" INSERT INTO posts(title ,content,published) 
    # VALUES (%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))

    # new_post = cursor.fetchone()
    # conn.commit()


    # print(**post.dict())
    new_post = model.Post(**post.dict())
    # new_post= model.Post(title=post.title,content = post.content,
    # published= post.published,)

    ## we have to save the changes
    
    db.add(new_post)
    db.commit()
    ## in sqlalchemy like sql dont have reutrning keyword
    # it has refresh
    db.refresh(new_post)
    return  new_post

# title str , content str ,category str,bool publihed

@app.get("/posts/latest") ## this show order is mattered
def get_latest():
    post = my_posts[len(my_posts)-1]
    return post


@app.get("/posts/{id}",response_model=schemas.PostCreate) 
def get_post(id: int,db:Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """,(str(id)))
    # post = cursor.fetchone()

    post = db.query(model.Post).filter(model.Post.id == id).first()
    # print(post)
    if not post :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
             detail= f"post with id: {id} was not found")

    return  post


## deleting post
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db)):
    
    # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """,(str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post = db.query(model.Post).filter(model.Post.id == id)



    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"post with id: {id} does not exist")
    
    post.delete(synchronize_session=False)
    db.commit()


    return Response(status_code=status.HTTP_204_NO_CONTENT)

## updataing post endpoint

@app.put("/posts/{id}",response_model=schemas.PostCreate)
def update_post(id : int,updated_post : schemas.PostCreate,db:Session = Depends(get_db)):
    # cursor.execute("""
    # UPDATE posts SET title = %s ,content = %s , published = %s WHERE id = %s 
    # RETURNING * """,(post.title , post.content , post.published,(str(id)),))
    # updated_post = cursor.fetchone()
    
    # conn.commit()
    query_post =db.query(model.Post).filter(model.Post.id == id) 
    post = query_post.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"post with id: {id} does not exist")
    
    query_post.update(updated_post.dict(),synchronize_session= False)


    db.commit()
    return query_post.first()

##creating user account  
@app.post("/users",status_code = status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db :Session = Depends(get_db)):


    # hash the password - use.password
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password


    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return new_user