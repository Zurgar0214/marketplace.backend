from typing import List
from dddpy.application.Models.editPostModel import EditPostModel
from dddpy.application.ResponseModels.postDetailResponseModel import PostDetailResponseModel
from dddpy.application.Models.postModel import CreatePostModel, PostOrdersModel
from sqlalchemy.orm import Session, selectinload
from dddpy.domain.schemas.image_dto import ImageDTO
from dddpy.domain.schemas.order_dto import OrderDTO
from dddpy.domain.schemas.post_dto import PostDTO
from dddpy.domain.schemas.qualification_dto import QualificationDTO
from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository

def create_post_service(post:CreatePostModel, db: Session):
        new_post = PostDTO(post.name, post.category, post.price, post.description, post.stock, post.status, post.createdUser)
        repository = GenericRepository(db, PostDTO)
        response = repository.add(new_post)
        return response.id

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
        orderRepository = GenericRepository(db, OrderDTO)
        qualificationrepository =  GenericRepository(db, QualificationDTO)
        userRepository = GenericRepository(db, UserDTO)
        imageRepository = GenericRepository(db, ImageDTO)
        post =  repository.get(id)
        orders = orderRepository.get_by_filter(post_id = post.id)
        qualifications: List[QualificationDTO] = []
        for order in orders:
               qualifications.append(qualificationrepository.get_by_filter(order_id = order.id))
        images = imageRepository.get_by_filter(post_id = post.id)
        user = userRepository.get(post.user_id)
        return PostDetailResponseModel(post,qualifications,images, user.phone)

def get_posts_by_user_service(user_id:str,db:Session):
       repository = GenericRepository(db, PostDTO)
       orderRepository = GenericRepository(db, OrderDTO)
       posts = repository.get_by_filter(user_id = user_id)
       postOrders : List[PostOrdersModel] = []
       for post in posts:
              orders =orderRepository.get_by_filter(post_id = post.id)
              response = PostOrdersModel(post,orders)
              postOrders.append(response)
       return postOrders

def get_posts_with_images_service(db: Session, limit: int, skip: int):
    query = db.query(PostDTO).options(selectinload(PostDTO.images))
    total = query.count()  # Get the total count of posts
    posts = query.offset(skip).limit(limit).all()
    return posts, total
