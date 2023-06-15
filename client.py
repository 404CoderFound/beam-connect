import socket


def client_program():
    host = socket.gethostname()  # Type your hostname (this is the hostname if using the same PC)
    port = 6666
    while True:
        with socket.socket() as client_socket:
            client_socket.connect((host, port))
            message = input("(help) -> ")
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(data)


if __name__ == '__main__':
    client_program()
