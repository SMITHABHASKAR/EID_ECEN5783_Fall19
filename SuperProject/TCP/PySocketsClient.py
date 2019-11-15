import sockets
import socket
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

    #client = Client()
    print("started Python client")
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    s.connect(("127.0.0.1", 1337))
    
    # poll the Node.JS server
    print("polling Node server")
    #response, addr = client.poll_server("Hello other world", server=('127.0.0.1', 1337))
    s.send(bytearray(b'hello'))
    #print("response received")
    #print (response, addr)

if __name__ == '__main__':
    main()
