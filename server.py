import socket
from flask import Flask, jsonify, request, render_template

HOST = "fuzytech.com"
PORT = 47000
app = Flask(__name__)
sock = socket.socket()

sock.bind((HOST, PORT))

sock.listen(20)

while True:
    print ("Waiting for connection")
    connection, address = sock.accept()
    connection.settimeout(10)
    while True:
        data = b""
        while True:
            tmp = connection.recv(1)
            if(tmp == b"`"):
                break
            data += tmp
        data = data.decode("ascii")
        if(data == "done"):
            break
        print (data)

    



