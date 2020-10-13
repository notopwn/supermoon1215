import socket

HOST = 'localhost'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as sock:
    sock.connect((HOST,PORT))

    while True:
        msg = input('enter message : ')
        if msg == '/quit':
            sock.sendall(msg.encode())
            break

        sock.sendall(msg.encode())
        data = sock.recv(1024)
        print('data from server : [%s]' %data.decode())

print('quitting client...')