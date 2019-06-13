class Card:
    def __init__ (self, number, cvc, expiry_year, expiry_month):
        self.__number = number
        self.__cvc = cvc
        self.__expiry_year = expiry_year
        self.__expiry_month = expiry_month
    
    @property
    def number (self):
        return self.__number

    @property
    def cvc (self):
        return self.__cvc

    @property
    def expiry_year (self):
        return self.__expiry_year

    @property
    def expiry_month (self):
        return self.__expiry_month
