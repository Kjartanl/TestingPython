# NOTE: Run this code separately after running 
# Networking_server.py to see them workin together.

import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host  = ''
port = 50000
connectionTuple = ('127.0.0.1', 50000)

# Connect to localhost, port 50000:
clientSock.connect(connectionTuple)

# Send as bytes:
clientSock.send(b"Hello, world!")

# Send as string:
clientSock.send("Hello, world!".encode("utf8"))

# Send the result of an input-request: 
clientSock.send(input("What do you want to send?").encode("utf8"))

clientSock.close()
