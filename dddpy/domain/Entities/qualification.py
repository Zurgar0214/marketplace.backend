from dddpy.domain.Entities.entity import Entity
class Qualification(Entity):
    def __init__(self,id: str, rate: int, comment: str):
        super().__init__(id)
        self.Rate : int = rate
        self.Comment : str = comment