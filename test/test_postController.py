import pytest
from fastapi.testclient import TestClient
from dddpy.application.Models.editPostModel import EditPostModel
from main import app  # reemplace esto con la ruta a su aplicación FastAPI

client = TestClient(app)

def test_get_posts():
    response = client.get("/getPosts")
    assert response.status_code == 200
    # Aquí puedes agregar más aserciones para verificar el contenido de la respuesta

def test_get_post_by_id():
    test_id = "some_test_id"  # Reemplaza esto con un ID de prueba válido
    response = client.get(f"/getPostById?id={test_id}")
    assert response.status_code == 200
    # Aquí puedes agregar más aserciones para verificar el contenido de la respuesta

def test_edit_post():
    test_post = EditPostModel(
        id="some_test_id",  # Reemplaza esto con un ID de prueba válido
        title="Test title",
        content="Test content"
    )
    response = client.put("/editPost", json=test_post.dict())
    assert response.status_code == 200
    # Aquí puedes agregar más aserciones para verificar el contenido de la respuesta