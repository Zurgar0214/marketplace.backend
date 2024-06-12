from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dddpy.application.Models.editPostModel import EditPostModel
from dddpy.application.Models.postModel import CreatePostModel
from dddpy.application.Models.userModel import UserModel
from dddpy.application.Services.postService import create_post_service, edit_post_service, get_postById_service, get_posts_by_user_service, get_posts_service
from dddpy.insfrastructure.Auth.jwt_depends import JWTBearer
from dddpy.insfrastructure.sqlite.database import get_db


post_router = APIRouter(prefix="/post",tags=["post"])
@post_router.post(
        "/createPost"
        )
async def create_post(post:CreatePostModel,db:Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
        return create_post_service(authorized,post,db)


@post_router.get(
     "/getPosts"
        )
async def get_posts(db:Session = Depends(get_db)):
        return get_posts_service(db)


@post_router.get(
     "/getPostById"
        )
async def get_postById( id: str,db:Session = Depends(get_db)):
        return get_postById_service(id,db)


@post_router.put(
     "/editPost"
        )
async def edit_post( editPost: EditPostModel ,db:Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
        return edit_post_service(editPost, db)

@post_router.get(
     "/getPostByUser"
        )
async def get_posts_by_user(user_id: str,db:Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
        return get_posts_by_user_service(user_id,db)

