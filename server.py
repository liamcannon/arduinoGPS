import socket

HOST = "fuzytech.com"
PORT = 47000

sock = socket.socket()

sock.bind((HOST, PORT))

sock.listen(20)

while True:
    print ("Waiting for connection")
    connection, address = sock.accept()
    data = b""
    while True:
        tmp = connection.recv(1)
        if(tmp == b"`"):
            break
        data += tmp
    data = data.decode("ascii")
    print (data)
    



