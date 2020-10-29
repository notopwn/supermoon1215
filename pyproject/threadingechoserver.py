import socket
import threading

port = 5000
localhost = ''

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        super().__init__()
        self.csocket = clientsocket
        print("New socket added: ",clientAddress)

    def run(self):
        print("connection from: ",clientAddress)
        msg = ''
        while True:
            data = self.csocket.recv(1024)
            msg = data.dedcode()
            if msg=='/quit':
                break
            print("from client",msg)
            self.csocket.send(bytes(msg,'UTF-8'))