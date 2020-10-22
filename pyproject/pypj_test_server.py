import socket import *
import _thread

r_buff = 1024
host_addr = '127.0.0.1'
port = 2500

def response(key) :
    return 'server responce message'

def handler(clientsock, addr):
    while True:

