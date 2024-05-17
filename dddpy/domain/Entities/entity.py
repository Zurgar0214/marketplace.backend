# domain/entity.py
from datetime import datetime

class Entity:
    def __init__(self, id: str):
        self.id = id
        self.creation_date = datetime.now()
        self.last_modified_date = datetime.now()

    def update_last_modified(self):
        self.last_modified_date = datetime.now()
