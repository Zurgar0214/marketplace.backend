# dto/user_dto.py
from datetime import datetime

class UserDTO:
    def __init__(self, id: str, username: str, email: str, creation_date: datetime, last_modified_date: datetime):
        self.id = id
        self.username = username
        self.email = email
        self.creation_date = creation_date
        self.last_modified_date = last_modified_date
