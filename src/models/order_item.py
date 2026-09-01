import uuid
from dataclasses import dataclass, field
@dataclass
class OrderItem:
    __id: uuid.uuid4()
    __product_category: str
    __order_id: int
    __quantity: int

    # def __init__(self, product_category, quantity, order_id):
    #     self.__id = uuid.uuid4()
    #     self.__product_category = product_category
    #     self.__order_id = order_id
    #     self.__quantity = quantity