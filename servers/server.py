import socket 

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432
print("STARTING SERVER ON " , SERVER_HOST , SERVER_PORT )
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    sock.bind((SERVER_HOST, SERVER_PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(data.decode("utf-8"))
            if not data:
                break
            conn.sendall(data)