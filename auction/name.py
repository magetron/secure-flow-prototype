class Name:
    def __init__ (self, first_name, middle_name, last_name):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name

    def get_full_name (self):
        return self.__first_name + " " + self.__middle_name + " " + self.__last_name

    @property
    def first_name (self):
        return self.__first_name

    @property
    def middle_name (self):
        return self.__middle_name

    @property
    def last_name (self):
        return self.__last_name

