from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dddpy.application.Models.qualificationModel import CreateQualificationModel
from dddpy.insfrastructure.sqlite.database import get_db


qualification_router = APIRouter(prefix="/qualification",tags=["qualification"])
@qualification_router.post(
        "/createQualification"
        )
async def create_qualification(qualification: CreateQualificationModel,db:Session = Depends(get_db)):
        return True