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
            self.__failed = None
            self.__bid = None

    @property
    def id (self):
        return self.__id

    @property
    def item (self):
        return self.__item

    @property
    def item (Self):
        return self.__started

    @property
    def bid (self):
        return self.__bid
        
    def start (self):
        if self.__failed == None:
            self.__started = True
            logging.info("Auction {} has started.".format(self.__id))
        else:
            logging.error("Auction {} failed to start.".format(self.__id))

    def stop (self):
        if self.__started:
            bid = self.__bid
            if (bid == None or (bid != None and self.item.base_price > bid.amount)):
                self.__failed = True
                logging.warning("Auction {} did not reach itme {} base price.".format(self.__id, self.__item.id))
            else:
                self.__failed = False
                self.__item.sold = True
            self.__started = False
            logging.info("Auction {} has ended with bid {} on item {}.".format(self.__id, self.__bid, self.__item.id))
        else:
            logging.error("Auction {} has not started yet.".format(self.__id)


    
