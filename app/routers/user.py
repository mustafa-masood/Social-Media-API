from fastapi import FastAPI, Response, status, HTTPException,Depends, APIRouter
from .. import schema,utils,models
from sqlalchemy.orm import Session 
from ..database import get_db

router = APIRouter(
   prefix="/users",
   tags=['Users']
) 

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.UserOut)
def create_users(user : schema.UserCreate,db: Session = Depends(get_db)): 
    #hash password
    hashed_pass = utils.hash(user.password)
    user.password = hashed_pass
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user) #for RETURNING
    return new_user

@router.get('/{id}', response_model=schema.UserOut)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")
    return user