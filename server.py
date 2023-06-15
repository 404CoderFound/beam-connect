import socket
import os
import sys
import threading
import requests as req

def handle_client(client_socket, address):
    args = sys.argv[1:]
    data = client_socket.recv(1024)
    message = data.decode('utf-8')
    print(f"Received message '{message}' from {address}")

    if message == "help":
        response = """files: Shows all files on server.
edit: Being able to edit files."""
        client_socket.send(response.encode())
    elif message == "files":
        contents = os.listdir()
        contents_str = "\n".join(contents)
        client_socket.send(contents_str.encode())
    elif message == "edit":
        ip = req.get('https://checkip.amazonaws.com').text.strip()
        client_socket.send(f"http://{ip}/edit?filename='file name that u want to edit'".encode())
        os.system("python3 flaskserver.py")
    else:
        client_socket.send("Command not recognized.".encode())

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (socket.gethostname(), 6666)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print(f"Server listening on {server_address}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        threading.Thread(target=handle_client, args=(client_socket, address)).start()

if __name__ == '__main__':
    main()
