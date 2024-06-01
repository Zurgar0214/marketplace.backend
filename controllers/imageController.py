from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from dddpy.application.Services.imageSerivice import upload_image_service
from dddpy.domain.schemas.image_dto import ImageDTO
from dddpy.insfrastructure.services.storageService import FirebaseStorage
from dddpy.insfrastructure.sqlite.database import get_db
from dddpy.insfrastructure.sqlite.repository.repository import GenericRepository


image_router = APIRouter(prefix="/image",tags=["image"])
@image_router.post(
        "/uploadImage"
        )
async def upload_image(image:UploadFile,idPost: str, db: Session = Depends(get_db))->str:
    return await upload_image_service(image, idPost, db)