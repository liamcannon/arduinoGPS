import socket

sock = socket.socket()

sock.connect(("fuzytech.com", 47000))

data = b'$GPGGA,181908.00,3404.7041778,N,07044.3966270,W,4,13,1.00,495.144,M,29.200,M,0.10,0000*40`'
sock.sendall(data)

sock.close()