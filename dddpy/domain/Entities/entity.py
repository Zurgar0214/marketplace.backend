from datetime import datetime
class Entity:
    def __init__(self, id: str):
        self.id: str = id
        self.creation_date: datetime
        self.last_modified_date :datetime


