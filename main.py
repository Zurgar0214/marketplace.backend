from fastapi import FastAPI, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from dddpy.application.Models.loginDataModel import UserLogin
from dddpy.application.Models.userModel import UserModel
from dddpy.domain.Entities.post import Post
from dddpy.insfrastructure.Auth.jwt_manage import encode_jwt
from dddpy.insfrastructure.sqlite.database import get_db, Base, engine
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository
from dddpy.insfrastructure.sqlite.schemas.post_dto import PostDTO
from dddpy.insfrastructure.sqlite.schemas.user_dto import UserDTO


app = FastAPI(debug=True)
Base.metadata.create_all(bind= engine)


@app.get(
        "/healthCheck",
        status_code=status.HTTP_200_OK
        )
async def healthCheck():
    '''app is already working!'''
    return {"message": "All works!"}


@app.post(
        "/createPost"
        )
async def create_post(post:Post, db: Session = Depends(get_db)):
        new_post = PostDTO(**post.__dict__)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return "true"

@app.get(
     "/getPosts"
        )
async def get_posts(db:Session = Depends(get_db)):
        repository = GenericRepository(db, PostDTO)
        return repository.get_all()
             
@app.post(
        "/createUser"
        )
async def create_post(user:UserModel, db: Session = Depends(get_db)):
        
        new_user = UserDTO(**user.__dict__)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return "true"
class PostRepository(GenericRepository[PostDTO]):
    def __init__(self, db_session: Session):
        super().__init__(db_session, Post)



@app.post("/login")
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
    
def validate_password(db_user: UserDTO, user:UserLogin):
    if db_user.password == user.password:
            
        token = get_token(User(**db_user.__dict__).__dict__)

        return token
    else:
        return None
    
def get_token(data: dict):
    return encode_jwt(data)