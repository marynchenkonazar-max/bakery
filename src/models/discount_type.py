import uuid
from dataclasses import dataclass, field
@dataclass
class DiscountType:
    __id: uuid.uuid4()

    # def __init__(self):
    #     self.__id = uuid.uuid4()