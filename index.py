import socket, threading


class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        print("New connection added: ", client_address)

    def run(self):
        print("Connection from : ", clientAddress)

        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            print("from client", msg)
            self.csocket.send(bytes(msg, 'UTF-8'))


LOCALHOST = "10.128.0.3"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    client_sock, clientAddress = server.accept()
    new_thread = ClientThread(clientAddress, client_sock)
    new_thread.start()
