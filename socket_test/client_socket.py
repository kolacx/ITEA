import socket

HOST = '127.0.0.1'
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

import time

while True:
    time.sleep(5)
    client_socket.send(b'I am client_socket')
    data = client_socket.recv(1024)
    print(data)