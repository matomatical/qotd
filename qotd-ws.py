import os
import asyncio

import websockets

import quotes

HOST = "" # allow all incoming connections
PORT = int(os.getenv('PORT', 17))

def main():
    # load quote list
    print("loading quotes list")
    q = quotes.QuoteList()
    async def qotd(websocket, path):
        print("got request", websocket.remote_address, path)
        print("sending quote", quote:=q.qotd())
        await websocket.send(quote)
        print("sent (disconnecting now)")

    print("will use port", PORT)
    print("setting up event loop (^C to quit)")
    asyncio.get_event_loop().run_until_complete(
            websockets.serve(qotd, HOST, PORT))
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nbye!")
