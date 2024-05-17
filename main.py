from fastapi import FastAPI, status, APIRouter, Depends
from sqlalchemy.orm import Session
from dddpy.domain.Entities.post import Post
from dddpy.insfrastructure.sqlite.database import get_db
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository
from dddpy.insfrastructure.sqlite.schemas.post_dto import PostDTO

app = FastAPI()
router = APIRouter()


@app.get(
        "/healthCheck",
        status_code=status.HTTP_200_OK
        )
async def healthCheck():
    '''app is already working!'''
    return {"message": "All works!"}


@app.get("/posts/{post_id}")
def get_post(post_id: str, db: Session = Depends(get_db)):
    repository = PostRepository(db)
    post = repository.get(post_id)
    return post.to_dto()

class PostRepository(GenericRepository[Post]):
    def __init__(self, db_session: Session):
        super().__init__(db_session, Post)