
from fastapi import FastAPI ,Body , Response,status,HTTPException,Depends,APIRouter
from .. import model,schemas,utils,auth2
from sqlalchemy.orm import Session
from ..database import  SessionLocal,get_db
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

##creating user account  
@router.post("/",status_code = status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db :Session = Depends(get_db)):


    # hash the password - use.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password


    new_user = model.User(**user.dict())
    db.add(new_user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    return new_user

@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id :int,db:Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id==id).first()


    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user with id : {id} does not exist")
    
    return user