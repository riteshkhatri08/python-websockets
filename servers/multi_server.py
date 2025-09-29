import selectors, socket


SERVER_PORT = 65432
SERVER_HOST = "127.0.0.1"

#  Create a selector
default_selector = selectors.DefaultSelector()


def read(conn, event):
    data = conn.recv(1024)
    if data:
        print("recevied data", repr(data), "from", conn)
        conn.send(data)
    else:
        print("closing", conn)
        default_selector.unregister(conn)
        conn.close()


# A callback method invoked for accepting connections on a socket
def accept(sock, event):
    conn, addr = sock.accept()
    print("accepted", conn, "from", addr)
    conn.setblocking(False)
    #  Now we register this connection in a selector
    # params : connection object and event to be monitored, the callback function to be triggered
    # when monitored event is triggererd
    default_selector.register(conn, selectors.EVENT_READ, read)


# Create a socket
sock = socket.socket()
# Bind this socket object to a address tuple
sock.bind((SERVER_HOST, SERVER_PORT))

sock.listen(100)
#  Set socket as non blocking
sock.setblocking(False)

# register this socket to a selector
# params : socket object, which event to listen for, callback function when event is received
default_selector.register(sock, selectors.EVENT_READ, accept)


#  While loop to continually listen for events on selector object
while True:
    selections = default_selector.select()
    #  as selections is a list of tuples of (key, event)
    for key, event in selections:
        # Data is the fucntion to be invoked for a matched key
        callback_function = key.data
        # callback functions accepts the socket (fileobj) that was registers and the event that was triggered for it
        callback_function(key.fileobj, event)
