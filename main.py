from auction.name import Name
from auction.card import Card
from auction.addr import Addr
from auction.user import User
from auction.item import Item
from auction.auction import Auction

def main ():
    auction = Auction(Item("iPhone XS Max", "iPhone A2104 256G", 6000))
    user = User(Name("Patrick", "", "Wu"), Card("1234567890", "123", 2099, 12), Addr("Room A, Road B", "London", "UK", "WC1E 6BT"))
    auction.start()
    user.bid(auction, 6010)
    user.bid(auction, 6020)
    auction.stop()

if __name__ == '__main__':
    main()
