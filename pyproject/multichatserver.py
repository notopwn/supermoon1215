from socket import *
from threading import *


class MultiChatServer:
    clients = []
    finalrecievedmessage=""

    def __init__(self):
        self.s_sock = socket(AF_INET, SOCK_STREAM)
        self.ip=''
        self.port = 5000
        self.s_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.s_sock.bind((self.ip,self.port))
        print("temporally waiting for connection")
        self.s_sock.listen(100)
        self.accept_client()

    def accept_client(self):
        while True:
            client = c_socket,(ip,port) = self.s_sock.accept()
            if client not in self.clients:
                self.clients.append(client)
            print(ip,':',str[port],'connected')
            t = Thread(target = self.recieve_messages, args = (c_socket,))
            t.start()

    def recieve_messages(self, c_socket):
        while True:
            try:
                incoming_message = c_socket.recv(1024)
                if not incoming_message:
                    break
            except:
                print("connection lost")

            else:
                self.finalrecievedmessage=incoming_message.decode('utf-8')
                print(self.finalrecievedmessage)
                self.send_all_clients(c_socket)
            c_socket.close()

    def send_all_clients(self, senders_socket):
        for client in self.clients:
            socket,(ip,port) = client
            if socket is not senders_socket:
                try:
                    socket.sendall(self.finalrecievedmessage.encode('utf-8'))
                except:
                    self.clients.remove(client)
                    print("{},{} connection quit".format(ip.port))

if __name__=="__main__":
    MultiChatServer()