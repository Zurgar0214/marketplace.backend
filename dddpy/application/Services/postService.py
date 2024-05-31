from fastapi import Depends
from dddpy.application.Models.editPostModel import EditPostModel
from dddpy.application.Models.postModel import CreatePostModel
from dddpy.insfrastructure.sqlite.database import get_db
from sqlalchemy.orm import Session
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository
from dddpy.insfrastructure.sqlite.schemas.post_dto import PostDTO

def create_post_service(post:CreatePostModel, db: Session):
        new_post = PostDTO(post.name, post.category, post.price, post.description, post.stock, post.status)
        repository = GenericRepository(db, PostDTO)
        response = repository.add(new_post)
        return response

def get_posts_service(db:Session):
        repository = GenericRepository(db, PostDTO)
        return repository.get_all()


def edit_post_service(editPost: EditPostModel,db:Session):
     repository = GenericRepository(db, PostDTO)

def get_postById_service( id: str, db:Session ):
        repository = GenericRepository(db, PostDTO)
        return repository.get(id)