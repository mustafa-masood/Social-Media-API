from fastapi import FastAPI, Response, status, HTTPException,Depends, APIRouter
from sqlalchemy import func
from .. import schema,models, oauth2
from sqlalchemy.orm import Session 
from ..database import get_db
from typing import Optional, List

router = APIRouter(
    prefix="/posts",
    tags=['Posts']    
)

# @router.get("/")
# def root(db: Session = Depends(get_db)):
#     return {"message": "Hello World"}

@router.get("/",response_model=List[schema.PostOut])
def get_posts(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return posts

# @app.post("/posts", status_code=status.HTTP_201_CREATED) # as it was showing 200 , when 201 must be shown for creation
# def create_posts(post : Post): 
#     post_dict = post.dict()
#     post_dict['id'] = randrange(0,1000000)
#     my_posts.append(post_dict)
#     # return {"data": "new post!"}
#     return {"data": post_dict}

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schema.ResponsePost)
def create_posts(post : schema.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)): 
#    cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
#    new_post = cursor.fetchone()
#    conn.commit()
    # print(current_user.email)
    new_post = models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #for RETURNING
    return new_post

@router.get("/{id}",response_model=schema.PostOut)
def get_post(id : int, response : Response,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)) : # this is to check if it is in int, if not it gives parameter feedback  
                                                # instead of internal  server error
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s""",(str(id)))
    # post = cursor.fetchone() 
    # post = find_post(id) 

    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    # post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post :
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        #  response.status_code = status.HTTP_404_NOT_FOUND
        #  return {"message": f"post with id: {id} was not found"}
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT) #used for deleting 204
def delete_post(id: int,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
     # deleting , by fetching index using method and simply using pop() method
    #  cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
    #  deleted_post = cursor.fetchone()
    #  conn.commit()
    #  index = find_index_post(id)
    deleted_post_query = db.query(models.Post).filter(models.Post.id == id)
    deleted_post = deleted_post_query.first()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not Authorized To perform requested action")

    deleted_post_query.delete(synchronize_session=False)
    db.commit()
    #  my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schema.ResponsePost)
def update_post(id: int, post : schema.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)): # post is a scheme a class that we are using to store and update
    #  index = find_index_post(id)
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published =%s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    post_query = db.query(models.Post).filter(models.Post.id==id)
    updated_post = post_query.first()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    if updated_post.owner_id != current_user.id:

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not Authorized To perform requested action")

    post_query.update(post.dict(),synchronize_session=False)
    #  post_dict = post.dict()
    #  post_dict['id'] = id
    #  my_posts[index] = post_dict
    # conn.commit()
    db.commit()
    return post_query.first()
     


# @app.post("/createposts")
# def create_posts(payLoad: dict = Body):
#     print(payLoad)
#     return {"new_post": f"title {payLoad['title']} content {payLoad['content']}"}

