class Addr:
    def __init__ (self, detail, city, country, post_code):
        self.__detail = detail
        self.__city = city
        self.__country = country
        self.__post_code = post_code

    def get_full_address (self):
        return self.__detail + ", " + self.__city + ", " + self.__country + ", " + self.__post_code

    @property
    def detail (self):
        return self.__detail

    @property
    def city (self):
        return self.__city

    @property
    def country (self):
        return self.__country

    @property
    def post_code (self):
        return self.__post_code


