from fastapi import FastAPI ,Body , Response,status,HTTPException# type: ignore

from pydantic import BaseModel
from typing import Optional

from random import randrange

app = FastAPI()

# using decorator help
# this is known as endpoint

class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating: Optional[int] = None




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
def hello():
    return {"data" : my_posts}


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post : Post): ## this is padentic model 
    ## to convert padentic into dict model we have to write
    post_dict = post.dict()
    post_dict['id'] = randrange(0,10000)
    my_posts.append(post_dict)
    return {"data": post_dict}

# title str , content str ,category str,bool publihed

@app.get("/posts/latest") ## this show order is mattered
def get_latest():
    post = my_posts[len(my_posts)-1]
    return {"dtail":post}


@app.get("/posts/{id}") ## this id field is called path parameters
def get_post(id: int,response : Response):
    print(type(id))
    post = find_post(int(id)) ## always path parameters return as string so we have to typecast into int!
    # if not post:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"message":f"post with id: {id} was not found"}

    if not post :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
             detail= f"post with id: {id} was not found")

    return {"post_detail": post}


## deleting post
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #deleting post
    # find the index in the arrray that has required id
    #my_post.pop(index)
    index = find_index_post(int(id))
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id : int,post : Post):
    index = find_index_post(int(id))

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} does not exist")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return{"data": post_dict}
    