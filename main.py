from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session
from dddpy.domain.Entities.post import Post
from dddpy.insfrastructure.sqlite.database import get_db, Base, engine
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository
from dddpy.insfrastructure.sqlite.schemas.post_dto import PostDTO


Base.metadata.create_all(bind= engine)
app = FastAPI(debug=True)


@app.get(
        "/healthCheck",
        status_code=status.HTTP_200_OK
        )
async def healthCheck():
    '''app is already working!'''
    return {"message": "All works!"}


@app.post("/createPost")
async def create_post(post: str, db: Session = Depends(get_db)):
    new_post = PostDTO(**post.__dict__)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return "true"

class PostRepository(GenericRepository[Post]):
    def __init__(self, db_session: Session):
        super().__init__(db_session, Post)