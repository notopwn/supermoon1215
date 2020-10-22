import socket import *
import _thread

r_buff = 1024
host_addr = '127.0.0.1'
port = 2500

def response(key) :
    return 'server responce message'

def handler(clientsock, addr):
    while True:
        data = clientsock.recv(r_buff)
        print('data : ' + repr(data))
        if not data : break
        clientsock.send(response('').encode())
        print('sent : ' + repr(response('')))

if __name__ == '__main__':
    end_point = (host_addr, port)
    serversock = socket(AF_INET, SOCK_STREAM)
