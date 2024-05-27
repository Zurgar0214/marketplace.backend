from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dddpy.application.Models.postModel import CreatePostModel, PostModel
from dddpy.application.Models.userModel import UserModel
from dddpy.domain.Entities.post import Post
from dddpy.insfrastructure.Auth.jwt_depends import JWTBearer
from dddpy.insfrastructure.sqlite.database import get_db
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository
from dddpy.insfrastructure.sqlite.schemas.post_dto import PostDTO


post_router = APIRouter(prefix="/post",tags=["post"])
@post_router.post(
        "/createPost"
        )
async def create_post(post:CreatePostModel, db: Session = Depends(get_db)):
        new_post = PostDTO(post.name, post.category, post.price, post.description, post.stock, post.status)
        print(type(new_post.price))
        repository = GenericRepository(db, PostDTO)
        return repository.add(new_post)
        

@post_router.get(
     "/getPosts"
        )
async def get_posts(db:Session = Depends(get_db)):
        repository = GenericRepository(db, PostDTO)
        return repository.get_all()