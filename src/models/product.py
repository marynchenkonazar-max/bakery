import uuid
import datetime
from dataclasses import dataclass, field
@dataclass
class Product:
    __id: uuid.uuid4()
    __product_category: str
    __created_at_time: datetime.datetime.now()
    __address: str

    # def __init__(self, product_category, address):
    #     self.__id = uuid.uuid4()
    #     self.__product_category = product_category
    #     self.__created_at_time = datetime.datetime.now()
    #     self.__address = address