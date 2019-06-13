import uuid

from .bid import Bid

class User:
    def __init__ (self, name, card, addr):
        self.__id = uuid.uuid1()
        self.__name = name
        self.__card = card
        self.__addr = addr

    @property
    def id (self):
        return self.__id
    
    @property
    def name (self):
        return self.__name

    @property
    def card (self):
        return self.__card

    @property
    def addr (self):
        return self.__addr

    def bid (self, auction, amount):
        Bid(self, auction, amount)
        
    
    
