# dto/qualification_dto.py
from datetime import datetime

class QualificationDTO:
    def __init__(self, id: str, user_id: str, post_id: str, score: int, comment: str, creation_date: datetime, last_modified_date: datetime):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
        self.score = score
        self.comment = comment
        self.creation_date = creation_date
        self.last_modified_date = last_modified_date
