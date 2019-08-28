import socket, threading


class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        print("New connection added: ", client_address)

    def run(self):
        print("Connection from : ", clientAddress)

        try:
            while True:
                data = self.csocket.recv(2048)
                if data is not None:
                    my_msg = data.decode()
                    print("from client", my_msg)
                    self.csocket.send(bytes(my_msg, 'UTF-8'))
        except socket.error as my_msg:
            print(f"Error sending to the client:{my_msg}")
            self.csocket.close()


LOCALHOST = "10.128.0.3"
PORT = 8080
try:
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

except socket.error as msg:
    print(f"Error binding Socket:{msg}")
