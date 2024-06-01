from dddpy.application.Models.editPostModel import EditPostModel
from dddpy.application.Models.postModel import CreatePostModel
from sqlalchemy.orm import Session
from dddpy.domain.schemas.post_dto import PostDTO
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository

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
     postToEdit = repository.get(editPost.id)
     postToEdit.editPost(editPost.price, editPost.description, editPost.stock, editPost.status)
     return repository.update(postToEdit)

def get_postById_service( id: str, db:Session ):
        repository = GenericRepository(db, PostDTO)
        # orderRepository = GenericRepository(db, OrderDTO)
        # qualificationrepository =  GenericRepository(db, QualificationDTO)
        # post =  repository.get(id)
        # orders = orderRepository.get_by_filter(postId = post.id)
        # qualifications: List[QualificationDTO] 
        return repository.get(id)