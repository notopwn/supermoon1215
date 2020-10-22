import socketserver
import threading

HOST = ''
PORT = 5000

class serverhandler(socketserver.BaseRequestHandler, threading.Thread):
    def handle(self):
        print('[%s] connected...'%self.client_address[0])

        try:
            while True:
                self.data = self.request.recv(1024)
                if self.data.decode() == '/quit':
                    print('[%s] quitted by user...' %self.client_address[0])
                    return

                print('[%s]'%self.data.decode())
                print('[%s]'%self.data)
                self.request.sendall(self.data)

        except Exception as e:
            print(e)

def runServer():
    print('starting Server...')

    try:
        server = socketserver.TCPServer((HOST, PORT), serverhandler)
        server.serve_forever()
        running = threading.Thread(target = serverhandler.handle())
    except KeyboardInterrupt:
        print('quitting...')

runServer()

