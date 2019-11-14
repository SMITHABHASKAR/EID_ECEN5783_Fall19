import sockets
# Test server with Python3:
from sockets.python3.server import Server
# Test client with Python3. Polls the Python3 server.
from sockets.python3.client import Client

class MyServer(Server):
    def act_on(self, data, addr):
        # Do something with data (in bytes) and return a string.
        return data

def main():
    #server = MyServer(listening_address=('127.0.0.1', 11112))
    # server.listen()

    client = Client()
    print("started Python client")
    #print ("polling Python server")
    #(response, addr) = client.poll_server("Hello world", server=('127.0.0.1', 11112))
    #print (response, addr)

    # poll the Node.JS server
    print("polling Node server")
    response, addr = client.poll_server("Hello other world", server=('127.0.0.1', 1337))
    print (response, addr)

if __name__ == '__main__':
    main()
