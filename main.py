from fastapi import FastAPI, status, APIRouter, Depends
from sqlalchemy.orm import Session
from dddpy.domain.Entities.post import Post
from dddpy.insfrastructure.sqlite.database import get_db, Base, engine
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository
from dddpy.insfrastructure.sqlite.schemas.post_dto import PostDTO

app = FastAPI()
Base.metadata.create_all(bind= engine)


@app.get(
        "/healthCheck",
        status_code=status.HTTP_200_OK
        )
async def healthCheck():
    '''app is already working!'''
    return {"message": "All works!"}


@app.post("/posts")
async def get_post(post_id: str, db: Session = Depends(get_db)):
    repository = PostRepository(db)
    post = repository.post()
    return post.to_dto()

class PostRepository(GenericRepository[Post]):
    def __init__(self, db_session: Session):
        super().__init__(db_session, Post)