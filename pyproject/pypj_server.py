import socketserver
import threading

HOST = ''
PORT = 5000

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('[%s] connected...'%self.client_address[0])

    def handle(self):

        try:
            while True:
                self.data = self.request.recv(1024)
                if self.data.decode() == '/quit':
                    print('[%s] quitted by user...' %self.client_address[0])
                    return

                print('[%s]'%self.data.decode())
                print('[%s]'%self.data)
                self.request.sendall(self.data)

            while True:

        except Exception as e:
            print(e)
    def a(self):
        x=threading.Thread(target=self.rund())
        x.start()

def runServer():
    print('starting Server...')

    try:
        server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('quitting Server...')

runServer()

