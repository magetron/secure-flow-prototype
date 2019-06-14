from auction.user import User
from auction.auction import Auction
from auction.auction_event import Auction_event

class bot:
    def __init__ (self, user, default_strategy):
        self.__alias = user
        self.__strategy = {}
        self.__default_strategy = default_strategy

    @property
    def alias (self):
        return self.__alias

    @property
    def default_startegy(self):
        return self.default_startegy

    def get_strategy_by_item_id (self, item_id):
        if item_id in self.__strategy:
            return self.__strategy[item_id]
        else:
            return self.__default_strategy

    def update_strategy (self, item, strat):
        self.__strategy[item.id] = strat

