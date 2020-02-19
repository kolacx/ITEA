import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
    )

try:
    server_socket.bind(
        (HOST, PORT)
        )
except socket.error as msg:
    print(msg)
    exit()

server_socket.listen(10)

def handler_client(client_socket):
    while True:
        data = client_socket.recv(1024) 

        if not data:
            break

        print(data)

        client_socket.send(data[::-1])

while True:
    client_socket, address = server_socket.accept()

    t = Thread(target=handler_client, args=(client_socket, ))
    t.start()
