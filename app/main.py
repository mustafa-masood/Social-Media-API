from urllib import response
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# the below command is no longer needed to create tables automatically when run using sqlalchemy becaure now we are using alembic

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#these array and functions are no longer needed

# my_posts = [{"title": "rigout watch" , "content": "reel video", "id": 1}, {"title": "rigout ring" , "content": "image", "id": 2}]   

# def find_post(id) :
#         for p in my_posts:
#              if p["id"] == id:
#                   return p
             
# def find_index_post(id):
#      for i, p in enumerate(my_posts):
#           if p['id'] == id:
#                return i

@app.get("/")
def root():
    return{"message","Hello World"}