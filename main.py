from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session
from dddpy.domain.Entities.post import Post
from dddpy.insfrastructure.sqlite.database import get_db, Base, engine
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository
from dddpy.insfrastructure.sqlite.schemas.post_dto import PostDTO


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
             

class PostRepository(GenericRepository[PostDTO]):
    def __init__(self, db_session: Session):
        super().__init__(db_session, Post)