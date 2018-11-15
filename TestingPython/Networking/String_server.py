
import socket


def main():

    print("Starting up...")
    HOST = ''
    PORT = 50002
    message_list = ['alpha', 'beta', 'gamma', 'delta', 'iota', 'cappa', 'lambda']

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))

    for msg in message_list:

        print("Waiting for a connection..")
        sock.listen(5)
        print("Found something?")

        conn, adr = sock.accept()
        received_msg = conn.recv(16)
        
        print("Received: %s" % received_msg)

        print("Sending: %s" % msg)
        sock.send(msg.encode("utf8"))


        conn.close()

main()


