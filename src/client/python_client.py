import socket


class TcpClient():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def establish_connection(self, host, port):
        self.socket.connect((host, port))
        print("Connection to ('{}', {}) established.".format(host, port))


def main():
    tcp_client = TcpClient()
    tcp_client.establish_connection("127.0.0.1", 9999)
    while True:
        message = input('Enter message here: ')
        message_encode = message.encode()
        tcp_client.socket.sendall(message_encode)
        while True:
            data = tcp_client.socket.recv(1024)
            if data.decode() == "done":
                break
            else:
                print(data.decode())


if __name__ == "__main__":
    main()
