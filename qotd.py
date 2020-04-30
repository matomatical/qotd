import csv
import os
import random
import socket
import time


HOST = "" # allow all incoming connections
PORT_SUPER  = 17
PORT_BACKUP = 1717
FILENAME = "quotes.txt"

def main():
    # load quote list
    print("loading quotes from", FILENAME)
    q = QuoteList(FILENAME)

    # set up server socket
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        print("attempting to bind to super port", PORT_SUPER)
        ssock.bind((HOST, PORT_SUPER))
    except PermissionError:
        print("re-trying to bing to normal port", PORT_BACKUP)
        ssock.bind((HOST, PORT_BACKUP))
    ssock.listen()
    print("listening... (^C to stop)")
    # process incoming connections
    while True:
        sock, addr = ssock.accept()
        print(addr, "connected...", end="", flush=True)
        quote = q.qotd()
        sock.sendall(quote.encode())
        sock.close()
        print(" quote sent!")


class QuoteList:
    def __init__(self, quotes_file):
        self.filename = quotes_file
        self._load()
    def _load(self):
        self.quotes = []
        self.loadtime = time.time()
        with open(self.filename) as f:
            text = f.read()
        pars = text.split('\n\n')
        for p in pars:
            lines = [l for l in p.splitlines() if l and not l[0]=="#"]
            if not lines: continue
            quote = ' '.join(lines)
            self.quotes.append(quote)
        print("loaded", len(self.quotes), "quotes")
    def qotd(self):
        # check if reload needed
        if self.loadtime < os.path.getmtime(self.filename):
            self._load()
        return random.choice(self.quotes)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nbye!")
