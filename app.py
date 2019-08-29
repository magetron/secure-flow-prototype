from flask import Flask, jsonify, request
from auction.name import Name
from auction.card import Card
from auction.addr import Addr
from auction.user import User
from auction.item import Item
from auction.auction import Auction
from auction.auction_event import Auction_event

app = Flask(__name__)

auctions = []

@app.route('v1/auction', methods=['GET', 'POST'])
def auctions():
    if request.method == 'GET':
        return jsonify(auctions)
    else:
        new_event = Auction_event()
        auctions.append(new_event)
        return jsonify(new_event.id)





