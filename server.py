import socketserver
from auction.auction_event import Auction_event

class AuctionHandler(socketserver.BaseRequestHandler):
    def setUp (self):
        self.users = []
        self.admin = None
        self.event = None

    def handle (self):
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        self.handler(self.data)
        self.request.sendall(self.data.upper())

    def handler (self, data):
        if data.startswith('identity '):
            self.identityhandler(data[9:])


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), AuctionHandler) as server:
        server.serve_forever()
