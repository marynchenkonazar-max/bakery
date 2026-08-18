import uuid
class ProductCategory:
    def __init__(self, name, price):
        self.__id = uuid.uuid4()
        self.__price = price
        self.__name = name
    def get_id(self):
        return self.__id
category = ProductCategory("vanila cake",80)

class Order:
    def __init__(self, created_at_time, order_items, price, discount, delivery_address):
        self.__id = uuid.uuid4()
        self.__price = price
        self.__created_at_time = created_at_time
        self.__order_items = order_items
        self.__discount = discount
        self.__delivery_address = delivery_address

class OrderItem:
    def __init__(self, product_category, quantity, order_id):
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
    def __init__(self, product_category, discount_type):
        self.__id = uuid.uuid4()
        self.__product_category = product_category
        self.__discount_type = discount_type
print(category.get_id())