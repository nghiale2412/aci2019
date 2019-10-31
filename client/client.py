import socket


def establish_connection(server_ip, server_udp_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((server_ip, server_udp_port))
    print("Successfully connect to server")
    return s


def main():
    client_socket = establish_connection("127.0.0.1", 27015)
    while True:
        message = input('Enter message here: ')
        message_encode = message.encode()
        client_socket.send(message_encode)
        data, server_address = client_socket.recvfrom(1024)
        print(data.decode())


if __name__ == "__main__":
    main()
