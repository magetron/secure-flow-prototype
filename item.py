import uuid

class Item:
    def __init__ (self, item_name, description, base_price):
        self.__id = uuid.uuid1()
        self.__item_name = product_name
        self.__description = description
        self.__base_price = base_price
        self.__sold = False

    @property
    def id (self):
        return self.__id

    @property
    def item_name (self):
        return self.__item_name

    @property
    def sold (self):
        return self.__sold



