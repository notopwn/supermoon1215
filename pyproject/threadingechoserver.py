import socket
import threading

port = 5000
localhost = 'localhost'

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        super().__init__()
        self.csocket = clientsocket
        self.clientAddress=clientAddress
        print("New socket added: ",clientAddress)

    def run(self):
        print("connection from: ",self.clientAddress)
        msg = ''
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            if msg=='/quit':
                break
            print("from client",msg)
            self.csocket.send(bytes(msg,'UTF-8'))
        print("Client at", self.clientAddress,"disconnected...")

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((localhost,port))
print("Server started")
print("Wating for client request...")
while True:
    server.listen(1)
    clientsock,clientAddress=server.accept()
    newthread=ClientThread(clientAddress,clientsock)
    newthread.start()