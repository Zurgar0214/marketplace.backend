from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dddpy.application.Models.userModel import UserModel
from dddpy.domain.Entities.post import Post
from dddpy.insfrastructure.sqlite.database import get_db
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository
from dddpy.insfrastructure.sqlite.schemas.post_dto import PostDTO


post_router = APIRouter(prefix="/post",tags=["post"])
@post_router.post(
        "/createPost"
        )
async def create_post(post:Post, db: Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
        new_post = PostDTO(**post.__dict__)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return "true"

@post_router.get(
     "/getPosts"
        )
async def get_posts(db:Session = Depends(get_db)):
        repository = GenericRepository(db, PostDTO)
        return repository.get_all()