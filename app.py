from flask import Flask, jsonify, request, abort
from auction.name import Name
from auction.card import Card
from auction.addr import Addr
from auction.user import User
from auction.item import Item
from auction.auction import Auction
from auction.auction_event import Auction_event

app = Flask(__name__)

auction_events = []
users = []
items = []

@app.route('/v1/auction_events', methods=['GET', 'POST'])
def auction_events_handler():
    if request.method == 'GET':
        return jsonify(auction_events)
    else:
        new_event = Auction_event()
        auction_events.append(new_event)
        return jsonify(new_event.id)

@app.route('/v1/users', methods=['GET', 'POST'])
def users_handler():
    if request.method == 'GET':
        return jsonify(users)
    else:
        first_name = request.form.get('first_name')
        middle_name = request.form.get('middle_name')
        last_name = request.form.get('last_name')
        card_number = request.form.get('card_number')
        cvc = request.form.get('cvc')
        expiry_year = request.form.get('expiry_year')
        expiry_month = request.form.get('expiry_month')
        addr_detail = request.form.get('addr_detail')
        city = request.form.get('city')
        postal = request.form.get('postal')
        new_user = User(Name(first_name, middle_name, last_name), Card(card_number, cvc, expiry_year, expiry_month), Addr(addr_detail, city, postal))
        users.append(new_user)
        return jsonify(new_user.id)

@app.route('/v1/items', methods=['GET', 'POST'])
def items_handler():
    if request.method == 'GET':
        return jsonify(items)
    else:
        name = request.form.get('name')
        description = request.form.get('description')
        base_price = request.form.get('base_price')
        new_item = Item(name, description, base_price)
        items.append(new_item)
        return jsonify(new_item.id)





