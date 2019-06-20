class Card:
    def __init__ (self, number, cvc, expiry_year, expiry_month):
        self.set_number(number)
        self.set_cvc(cvc)
        self.set_expiry_time(expiry_year, expiry_month)

    def set_number (self, number):
        if len(number) != 16 or not number.isnumeric():
            raise Exception("Card number should be 16 digits long")
        else:
            self.__number = number

    def set_cvc (self, cvc):
        if len(cvc) != 3 or not cvc.isnumberic():
            raise Exception("Card CVC should 3 digits long")
        else:
            self.__cvc = cvc

    def set_expiry_time (self, expiry_year, expiry_month):
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
