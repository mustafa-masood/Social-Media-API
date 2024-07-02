from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
# from pydantic.types import conint
from typing_extensions import Annotated
from pydantic import BaseModel, Field

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True

class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class ResponsePost(PostBase):
    id:int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: ResponsePost
    votes: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    # dir is the direction of vote
    # which means that if it is 1, and the post has not been
    # voted, so it will vote post
    # however, if dir = 0, and the post is voted , so it will
    #r remove the vote from the post, and so on checks like it
    dir: Annotated[int, Field(strict=True, ge=0,le=1)]