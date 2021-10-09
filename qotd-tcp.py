import socket

import quotes

HOST = "" # allow all incoming connections
PORT = 17

def main():
    # load quote list
    print("loading quotes list...")
    q = quotes.QuoteList()

    # set up server socket
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("attempting to bind to port", PORT)
    ssock.bind((HOST, PORT))
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

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nbye!")
