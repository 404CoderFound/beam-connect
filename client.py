import socket


def client_program():
  host = socket.gethostname()  # Type ur hostname (this is the hostname if using same pc)
  port = 6666
  while True:
    try:
      client_socket = socket.socket()

      client_socket.connect((host, port))
      message = input("(help) -> ")
      client_socket.send(message.encode())
      data = client_socket.recv(1024).decode()
      print(data)
    finally:
      client_socket.close()



if __name__ == '__main__':
  client_program()
