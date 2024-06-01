from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from dddpy.domain.schemas.image_dto import ImageDTO
from dddpy.insfrastructure.services.storageService import FirebaseStorage
from dddpy.insfrastructure.sqlite.database import get_db
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository


image_router = APIRouter(prefix="/image",tags=["image"])
@image_router.post(
        "/uploadImage"
        )
async def upload_image(image:UploadFile,idPost: str, db: Session = Depends(get_db))->str:
    firebase = FirebaseStorage()
    repository = GenericRepository(db, ImageDTO)
    url = await firebase.save(file= image)
    newImage = ImageDTO(url,idPost)
    repository.add(newImage)
    return url