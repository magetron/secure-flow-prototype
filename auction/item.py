import uuid

class Item:
    def __init__ (self, name, description, base_price):
        self.__id = uuid.uuid1()
        self.__name = name
        self.__description = description
        self.__base_price = base_price
        self.__sold = False

    @property
    def id (self):
        return self.__id

    @property
    def name (self):
        return self.__name

    @property
    def description (self):
        return self.__description

    @property
    def base_price (self):
        return self.__base_price

    @property
    def sold (self):
        return self.__sold

    def update_sold (self, sold):
        self.__sold = sold
