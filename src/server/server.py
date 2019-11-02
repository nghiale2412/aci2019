import socket
import asyncio
import struct
import math


def init_socket_server():
	server_udp_port = 27015
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# bind listener to specified port
	server_socket.bind(("", server_udp_port))
	print("Server started successfully.")
	return server_socket


async def on_connection_request(socket):
	print("Listening for connection from client...")
	while True:
		try:
			# read request from client(s)
			request, address = socket.recvfrom(1024)
			print("Received connection from {}".format(address))
			message = "Here is your data"

			# send data to client
			socket.sendto(message.encode(), address)
		except Exception as err:
			raise err


async def main():
	# creating server socket
	server_socket = init_socket_server()

	# start a task that will listen for connection from clients (async)
	task = loop.create_task(on_connection_request(server_socket))
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

