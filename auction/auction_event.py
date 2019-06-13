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
        if list(already_exsist) != []:
            print("ERROR: Auction {} is already in the list.".format(new_auction.id))
        else:
            print("INFO: Auction {} appended to Auction Event {}.".format(new_auction.id, self.__id))
            self.__list.append(new_auction)

    def get_last_auction_status_by_item_id (self, item_id):
        item_auction = list(filter(lambda auction: auction.item.id == item_id, self.__list))
        if list(item_auction) == []:
            status = "Item {} has no auctions".format(item_id)
        else:
            item_auction = list(item_auction)[-1]
            status = "Lastest auction for item {} {} is {}. \n".format(item_id, item_auction.item.name, item_auction.id)
            if item_auction.failed:
                status += "The above auction has failed due to not met of base price. \n"
            elif item_auction.started:
                status += "The above auction has started with "
                if item_auction.bid == None:
                    status += "no bid. \n"
                else:
                    status += "top bid of {} from {}. \n".format(item_auction.bid.amount, item_auction.bid.bidder)
            else:
                status += "The above auction has ended with item sold of {} to {}. \n".format(item_auction.bid.amount, item_auction.bid.bidder.name.get_full_name())

        return status

                    
            
