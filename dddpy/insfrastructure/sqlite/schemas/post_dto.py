# dto/post_dto.py
from datetime import datetime

class PostDTO:
    def __init__(self, id: str, title: str, content: str, creation_date: datetime, last_modified_date: datetime):
        self.id = id
        self.title = title
        self.content = content
        self.creation_date = creation_date
        self.last_modified_date = last_modified_date
