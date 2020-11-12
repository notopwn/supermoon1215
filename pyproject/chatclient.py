import socket

HOST = 'localhost'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as sock:
    sock.connect((HOST,PORT))

    while True:
        msg = input('enter message : ')
        sock.sendall(msg.encode())
        data = sock.recv(1024)
        if msg!=data.decode():
            print('data from server : [%s]' % data.decode())

        if msg == '/quit':
            sock.sendall(msg.encode())
            break


print('quitting client...')