import uuid
from dataclasses import dataclass, field
@dataclass
class Address:
    __id: uuid.uuid4()
    __post_index: int
    __street:str
    __city: str
    __latitude: float
    __longitude: float

    # def __init__(self, post_index, street, city, latitude, longitude):
    #     self.__id = uuid.uuid4()
    #     self.__post_index = post_index
    #     self.__street = street
    #     self.__city = city
    #     self.__latitude = latitude
    #     self.__longitude = longitude