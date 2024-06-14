# test_postService.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dddpy.domain.schemas.user_dto import UserDTO
from dddpy.insfrastructure.sqlite.database import Base, get_db
from dddpy.application.Services.postService import create_post_service, get_posts_by_user_service, get_posts_service, edit_post_service, get_postById_service
from dddpy.application.Models.postModel import CreatePostModel
from dddpy.application.Models.editPostModel import EditPostModel
from dddpy.domain.schemas.post_dto import PostDTO
from dddpy.domain.schemas.order_dto import OrderDTO
from dddpy.domain.schemas.qualification_dto import QualificationDTO
from dddpy.domain.schemas.image_dto import ImageDTO

# Configuración de la base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)

# Configurar la base de datos de prueba
@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_post_service(db: Session):
    post_data = CreatePostModel(
        name="Test Post",
        category=1,
        price=100.0,
        description="A test post",
        stock=10,
        status=1,
        createdUser="e8007d1f-458b-4be6-8f07-e3371219d705"
    )
    post_id = create_post_service(post_data, db)
    assert post_id is not None
    post = db.query(PostDTO).filter(PostDTO.id == post_id).first()
    assert post is not None
    assert post.name == post_data.name

def test_get_posts_service(db: Session):
    posts = get_posts_service(db)
    assert len(posts) > 0
    assert posts[0].name == "Test Post"

def test_edit_post_service(db: Session):
    post = db.query(PostDTO).first()
    edit_post_data = EditPostModel(
        id=post.id,
        price=150.0,
        description="An updated post",
        stock=5,
        status=1
    )
    updated_post = edit_post_service(edit_post_data, db)
    post = db.query(PostDTO).filter(PostDTO.id == updated_post.id).first()
    assert post is not None
    assert post.price == edit_post_data.price
    assert post.description == edit_post_data.description
    assert post.stock == edit_post_data.stock

def test_get_postById_service(db: Session):
    post = db.query(PostDTO).first()
    post_detail = get_postById_service(post.id, db)
    assert post_detail.id == post.id
    assert post_detail.name == post.name

def test_get_post_by_user_service(db: Session):
    # Primero, crea un usuario y un post asociado a ese usuario
    user = UserDTO(name="Test For Posts", lastName="User", email="testuser@example.com", phone="32344444", password="Admin1234")
    post = PostDTO(name="Test Post With User", category=1, price=150.0, description="A test post", stock=10, status=1, createdUser=user.id)
    db.add(user)
    db.add(post)
    db.commit()

    # Luego, llama a tu servicio get_post_by_user
    posts = get_posts_by_user_service(user.id, db)

    # Asegúrate de que el servicio devuelve el post correcto
    assert len(posts) == 1
    assert posts[0].id == post.id
    assert posts[0].price == post.price
    assert posts[0].description == post.description
    assert posts[0].stock == post.stock
