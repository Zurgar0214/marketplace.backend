from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dddpy.application.Models.loginDataModel import UserLogin
from dddpy.application.Services.authService import validate_password
from dddpy.insfrastructure.sqlite.database import get_db
from sqlalchemy.orm import Session

from dddpy.insfrastructure.sqlite.schemas.user_dto import UserDTO


auth_router = APIRouter(prefix="/auth",tags=["auth"])
@auth_router.post("/login")
def login(user: UserLogin, db:Session = Depends(get_db)):
    db_user = db.query(UserDTO).filter(UserDTO.email == user.email).first()

    if db_user:
        token = validate_password(db_user, user)
        
        if token:
            return JSONResponse(content={"token": token}, status_code=200)
        else:
            return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)
        
    else:
        return JSONResponse(content={"message": "User does not exist"}, status_code=401)