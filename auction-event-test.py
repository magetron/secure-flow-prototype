import unittest

from auction.name import Name
from auction.card import Card
from auction.addr import Addr
from auction.user import User
from auction.item import Item
from auction.auction import Auction
from auction.auction_event import Auction_event

class Auction_event_test (unittest.TestCase):
    
    def setUp (self):
        self.auction_event = Auction_event()
        self.user = User(Name("Patrick", "", "Wu"), Card("1234567890", "123", 2099, 12), Addr("Room A, Rd B", "London", "UK", "WC1E 6BT"))
        self.item1 = Item("iPhone XS Max Space Grey", "A2104 256G", 6000)
        self.item2 = Item("Google Pixel 3 XL", "G013C 64G", 5000)

    def tearDown (self):
        self.auction_event = None

    def testAddAuction (self):
        auction1 = Auction(self.item1)
        auction2 = Auction(self.item2)
        self.auction_event.add_new_auction(auction1)
        self.auction_event.add_new_auction(auction2)
        self.assertListEqual(self.auction_event.list, [auction1, auction2])

    def testAddAuctionFail (self):
        auction1 = Auction(self.item1)
        self.auction_event.add_new_auction(auction1)
        self.auction_event.add_new_auction(auction1)
        self.assertListEqual(self.auction_event.list, [auction1])
        
    def testLastAuctionSearch (self):
        auction1 = Auction(self.item1)
        auction2 = Auction(self.item2)
        self.auction_event.add_new_auction(auction1)
        self.auction_event.add_new_auction(auction2)
        self.auction_event.list[0].start()
        self.auction_event.list[1].start()
        self.user.bid(self.auction_event.list[0], 6001)
        self.user.bid(self.auction_event.list[1], 5500)
        self.user.bid(self.auction_event.list[1], 5750)
        self.auction_event.list[0].stop()
        print(self.auction_event.get_last_auction_status_by_item_id(self.item1.id))
        print(self.auction_event.get_last_auction_status_by_item_id(self.item2.id))
    
    def testLastAuctionSearchNone (self):
        auction1 = Auction(self.item1)
        self.auction_event.add_new_auction(auction1)
        print(self.auction_event.get_last_auction_status_by_item_id(self.item2.id))


if __name__ == '__main__':
    unittest.main()
