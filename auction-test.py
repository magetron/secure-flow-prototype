import unittest

from auction.name import Name
from auction.card import Card
from auction.addr import Addr
from auction.user import User
from auction.item import Item
from auction.auction import Auction

class AuctionTest (unittest.TestCase):

    def setUp (self):
        self.auction = Auction(Item("iPhone XS Max", "iPhone A2104 256G", 6000))
        self.user = User(Name("Patrick", "", "Wu"), Card("1234567890", "123", 2099, 12), Addr("Room A, Road B", "London", "UK", "WC1E 6BT"))

    def tearDown (self):
        self.auction = None

    def testStart (self):
        self.auction.start()
        self.assertTrue(self.auction.started)

    def testSuccess (self):
        self.auction.start()
        self.user.bid(self.auction, 6010)
        self.auction.stop()
        self.assertFalse(self.auction.started)
        self.assertFalse(self.auction.failed)
        self.assertTrue(self.auction.item.sold)
        

    def testNotStart (self):
        self.auction.stop()
        self.assertFalse(self.auction.started)
        self.assertFalse(self.auction.failed)
        self.assertIsNone(self.auction.bid)

if __name__ == '__main__':
    unittest.main()
