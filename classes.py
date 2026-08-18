import uuid
import datetime
class ProductCategory:
    def __init__(self, name, price):
        self.__id = uuid.uuid4()
        self.__price = price
        self.__name = name
    def get_id(self):
        return self.__id


class Order:
    def __init__(self, order_items, price, discount, address):
        self.__id = uuid.uuid4()
        self.__price = price
        self.__created_at_time = datetime.datetime.now()
        self.__order_items = order_items
        self.__discount = discount
        self.__address = address

class OrderItem:
    def __init__(self, product_category, quantity, order_id):
        self.__id = uuid.uuid4()
        self.__product_category = product_category
        self.__order_id = order_id
        self.__quantity = quantity

class Address:
    def __init__(self, post_index, street, city, latitude, longitude):
        self.__id = uuid.uuid4()
        self.__post_index = post_index
        self.__street = street
        self.__city = city
        self.__latitude = latitude
        self.__longitude = longitude

class DiscountType:
    def __init__(self):
        self.__id = uuid.uuid4()

class Product:
    def __init__(self, product_category, address):
        self.__id = uuid.uuid4()
        self.__product_category = product_category
        self.__created_at_time = datetime.datetime.now()
        self.__address = address
