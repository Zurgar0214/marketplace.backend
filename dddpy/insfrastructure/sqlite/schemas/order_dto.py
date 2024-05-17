# dto/order_dto.py
from datetime import datetime

class OrderDTO:
    def __init__(self, id: str, user_id: str, total_amount: float, creation_date: datetime, last_modified_date: datetime):
        self.id = id
        self.user_id = user_id
        self.total_amount = total_amount
        self.creation_date = creation_date
        self.last_modified_date = last_modified_date
