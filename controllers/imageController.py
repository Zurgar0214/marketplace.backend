from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from dddpy.insfrastructure.services.storageService import FirebaseStorage
from dddpy.insfrastructure.sqlite.database import get_db


image_router = APIRouter(prefix="/image",tags=["image"])
@image_router.post(
        "/uploadImage"
        )
async def upload_image(image:UploadFile, db: Session = Depends(get_db))->str:
    firebase = FirebaseStorage()
    return await firebase.save(file= image)