class User:
    def __init__ (self, name, card, addr):
        self.__name = name
        self.__card = card
        self.__addr = addr

    @property
    def name (self):
        return self.__name;

    @property
    def card (self):
        return self.__card;

    @property
    def addr (self):
        return self.__addr;

        
    
    
