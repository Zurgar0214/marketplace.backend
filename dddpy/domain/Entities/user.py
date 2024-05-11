from typing import List
from dddpy.domain.Entities.post import Post;
from dddpy.domain.Entities.qualification import Qualification;
class User:
    def __init__(self, name : str, lastName: str, email: str, phone: str, password: str):
        self.Name : str = name
        self.LastName: str = lastName
        self.Email: str = email
        self.Phone: str = phone
        self.Password: str = password
        self.Posts : List[Post] = []
        self.Qualifications: List[Qualification] = []
