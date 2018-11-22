
import socket


def main():

    print("Starting up...")
    HOST = ''
    PORT = 50002
    message_list = ['alpha', 'beta', 'gamma', 'delta', 'iota', 'cappa', 'lambda']

    for msg in message_list:
        print(msg)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        
        print("about to listen..")
        sock.listen(1)
        conn, adr = sock.accept()

        conn.send(msg.encode("utf8"))
        conn.close()
main()


