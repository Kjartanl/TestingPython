
import socket

def run_server():
    # Constructor for socket
    # note: AF_INET =  IPV4; AF_INET6 is for IPC6. 
    # socket.SOCK_STREAM specifies to use TCP (as op. to UDP)
    # (This is the easiest an fastest way to set up communication) 
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host  = ''
    port = 50000
    serverSock.bind((host, port))

    print("Sock is now ready: %s" %serverSock)


    # Listen for connections
    serverSock.listen(3) # Accept up to 3 clients to connect at once

    print("Ok, now ready to listen for clients..")

    #Actually open the socket for connections:
    #(connSock will contain info about a connection once established)
    connSock, address = serverSock.accept()

    # Accept a message of up to 16 bytes:
    received = connSock.recv(16)

    while received != '':
        input("Received: %s" %received)
        received = connSock.recv(16)

    # Print the data received:
    input("Received empty - done!")


run_server()







