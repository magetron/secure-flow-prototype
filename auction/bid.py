import uuid

class Bid:
    def __init__(self, bidder, auction, amount):
        if not auction.started:
            print("WARNING: Auction {} has not started.".format(auction.id))
        elif auction.bid != None and auction.bid.amount >= amount:
            print("ERROR: Bid not successful. Not higher than highest bid.")
        else:
            self.__id = uuid.uuid1()
            self.__bidder = bidder
            self.__amount = amount
            self.__auction = auction
            self.__auction.update_bid(self)
            print("INFO: {} bids {} for auction {} successful.".format(bidder.name.get_full_name(), amount, auction.id))

    @property
    def id (self):
        return self.__id

    @property
    def bidder (self):
        return self.__bidder

    @property
    def amount (self):
        return self.__amount

    @property
    def aunction (self):
        return self.__auction

