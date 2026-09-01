import uuid
from dataclasses import dataclass, field
@dataclass
class User:
    __id: uuid.uuid4()
    __name: str
    __number: int
    __gmail: str
    __address: list

    # def __init__(self, name, number, gmail):
    #     self.__id = uuid.uuid4()
    #     self.__name = name
    #     self.__number = number
    #     self.__gmail = gmail
    #     self.__address = []