import uuid
import datetime
from dataclasses import dataclass, field
@dataclass
class Order:
    __id: uuid.uuid4()
    __price: float
    __created_at_time: datetime.datetime.now()
    __order_items: list
    __discount: classmethod
    __address: str

    # def __init__(self, order_items, price, discount, address):
    #     self.__id = uuid.uuid4()
    #     self.__price = price
    #     self.__created_at_time = datetime.datetime.now()
    #     self.__order_items = order_items
    #     self.__discount = discount
    #     self.__address = address