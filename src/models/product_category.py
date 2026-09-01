import uuid
from dataclasses import dataclass, field
@dataclass
class ProductCategory:
    __id: uuid.uuid4()
    __price: float
    __name: str
    @property
    def id(self):
        return self.__id

    # def __init__(self, name, price):
    #     self.__id = uuid.uuid4()
    #     self.__price = price
    #     self.__name = name
    # def get_id(self):
    #     return self.__id