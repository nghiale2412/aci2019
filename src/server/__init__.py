import socket
import asyncio


class TcpServer():
	def __init__(self, host, port):
		self.server_host = host
		self.server_port = port
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# bind listener to specified port
		self.server_socket.bind((self.server_host, self.server_port))

		print("Server setup successfully.")

	def start(self):
		# start listening for incoming connection
		self.server_socket.listen(1)
		print("Listening for connection from client...")

		while True:
			# accept connection from client
			conn, client_address = self.server_socket.accept()
			try:
				print("Received connection from {}".format(client_address))
				while True:
					# read request from client(s)
					data = conn.recv(1024)
					print("Received {!r}".format(data.decode()))

					if data:
						message = "Here is your data"
						# send data to client
						conn.sendall(message.encode())
					else:
						break

			finally:
				conn.close()


async def main():
	# setup server: TcpServer(host, port)
	tcp_server = TcpServer("", 27015)
	# start a task that will listen for connection from clients asynchronously
	task = loop.create_task(tcp_server.start())
	await asyncio.wait(task)

if __name__ == "__main__":
	try:
		# create an event loop for asyncio
		loop = asyncio.get_event_loop()

		# start the loop until main function completed its job
		loop.run_until_complete(main())
	except Exception as err:
		raise err
	finally:
		# close loop on finish
		loop.close()

