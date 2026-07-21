from fastapi import APIRouter, Depends, status,HTTPException,Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..import database,schemas,model,utils,auth2
from .import user


router = APIRouter(tags=['Authentication'])


@router.post('/login',response_model=schemas.Token)
def login(user_credentails: OAuth2PasswordRequestForm = Depends(),db :Session = Depends(database.get_db)):


    #{ this user cresdential return
    #    "username" = "blah"
    #     "password" = "35975"
    #}

    user = db.query(model.User).filter(model.User.email == user_credentails.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
        detail=f"Invalid credentials")
    
    if not utils.verify(user_credentails.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")
    
    access_token = auth2.create_access_token(data = {"user_id": user.id})
# create a token
# return token
    return {"access_token":access_token,"token_type":"bearer"}