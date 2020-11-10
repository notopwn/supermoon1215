import socketserver
import threading
import random

HOST =''
PORT = 5000

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('%s connected'%self.client_address[0])

        try:
            while True:
                self.data = self.request.recv(1024)
                if self.data.decode() == '/quit':
                    print('%s disconnected by user'%self.client_address[0])
                    return
                if self.data.decode()=='/start':
                    print('game started')


                print('%s'%self.data.decode())
                self.request.sendall(self.data)
        except Exception as e:
            print(e)

def runServer():
    print('running echo server.')
    print('to quit echo server, press command+C')

    try:
        server = socketserver.TCPServer((HOST,PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('quitting echo server;;;')

runServer()
threading.Thread(target = runServer())