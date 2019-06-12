from user import User
from name import Name
from card import Card
from addr import Addr

def new_name ():
    first_name = input("first name: ")
    middle_name = input("middle name: ")
    last_name = input("last name: ")
    return Name(first_name, middle_name, last_name)

def new_card ():
    number = input("card number: ")
    cvc = input("cvc: ")
    expiry_year = input("expiry year: ")
    expiry_month = input("expiry month: ")
    return Card(number, cvc, expiry_year, expiry_month)

def new_addr ():
    detail = input("addr detail: ")
    city = input("city: ")
    country = input("country: ")
    post_code = input("post_code: ")
    return Addr(detail, city, country, post_code)

def new_user ():
    return User(new_name(), new_card(), new_addr())

def main ():
    user = new_user()
    print(user.name.get_full_name() + " " + user.addr.get_full_address())

if __name__ == '__main__':
    main()
    
