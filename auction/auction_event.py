import uuid
import logging

logging.getLogger().setLevel(logging.INFO)

class Auction_event:
    def __init__ (self):
        self.__id = uuid.uuid1()
        self.__list = []

    @property
    def id (self):
        return self.__id

    @property
    def list (self):
        return self.__list

    def add_new_auction (self, new_auction):
        already_exsist = filter(lambda auction: auction.id == new_auction.id, self.__list)
        if already_exsist:
            logging.error("Auction {} is already in the list.".format(new_auction.id))
        else:
            self.__list.append(auction)

    def get_last_auction_status_by_item_id (self, item_id):
        item_auction = filter(lambda auction: auction.item.id == item_id, self.auctions)[-1]
        if item_auction == None:
            status = "Item {} has no auctions".format(item_id)
        else:
            status = "Lastest auction for item {} {} is {}. \n".format(item_id, item_auction.item.name, item_auction.id)
            if item_auction.failed:
                status += "The above auction has failed due to not met of base price. \n"
            elif item_auction.started:
                status += "The above auction has started with "
                if item_auction.bid == None
                    status += "no bid. \n"
                else
                    status += "top bid of {} from {}. \n".format(item_auction.bid.amount, item_auction.bid.bidder)
            else:
                status += "The above auction has ended with item sold of {} to {}. \n".format(item_auction.bid.amount, item_auction.bid.bidder)

        return status

                    
            
