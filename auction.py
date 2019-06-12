import uuid
import logging

logging.getLogger().setLevel(logging.INFO)

class Auction:
    def __init (self, item):
        if item.sold:
            logging.error("Item {} already sold.".format(item.name))
        else:
            self.__id = uuid.uuid1()
            self.__item = item
            self.__started = False
            self.__bid = None

    
