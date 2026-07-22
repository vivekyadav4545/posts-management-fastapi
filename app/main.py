from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware ## this is for the cors

from .import model
from .database import engine
from .routers import post,user,auth,vote
from .config import settings
from fastapi.responses import RedirectResponse



# model.Base.metadata.create_all(bind=engine)

app = FastAPI()

orgins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return RedirectResponse(url="/docs")



@app.get("/")
def root():
    return {"message":"Hello World!"}