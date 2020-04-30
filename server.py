import socket
import _thread
import json
import asyncio
import websockets

HOST = "fuzytech.com"
PORT = 47000
APIPORT = 47001
dataPoints=[1, 1, 3, 4, 5]

#async def apiServ(websocket, path):
 #   while True:
  #      await websocket.send(dataPoints)

#start_server = websockets.serve(apiServ, HOST, APIPORT)

#def runApi():
 #   asyncio.get_event_loop().run_until_complete(websockets.serve(start_server))
  #  asyncio.get_event_loop().run_forever()  

#_thread.start_new_thread(runApi, ())


sock = socket.socket()
sock.bind((HOST, PORT))

sock.listen(20)

def handleGet(connection, addr):
    print('Handle Get')
    connection.recv(4000)
    tmp = ("var data_points = " + json.dumps(dataPoints)+";").encode("utf-8")
    with open('dataPoints/points.json', 'w') as outfile:
        json.dump(dataPoints, outfile)
    connection.sendall(tmp)

def handleRecv(connection, addr):
    print('Handle Recieved')
    connection.settimeout(100)
    try:
        while True:
            data = b""
            while True:
                tmp = connection.recv(1)
                if(tmp == b"`"):
                    break
                data += tmp
            data = data.decode("utf-8")
            if(data == "done"):
                break
            print(data)
        tmpPointsStr = data.split(';')
        tmpPoints = [float(tmpPointsStr[0]), float(tmpPointsStr[1])]
        dataPoints.append([tmpPoints[0], tmpPoints[1]])
    except:
        print("Close")
        connection.close()
    tmp = ("var data_points = " + json.dumps(dataPoints)+";").encode("utf-8")
    outFile = open("dataPoints/points.js", "w")
    outFile.write(tmp)
    outFile.close()


def handle(connection, addr):
    connection.settimeout(100)
    print("connected to ", address)
    try:
        data = b""
        while True:
            tmp = connection.recv(1)
            if(tmp == b"`"):
                break
            data += tmp
        if data == b'data':
            handleRecv(connection, address)
        elif data == b'GET':
            handleGet(connection, address)
        else:
            print("Close")
            connection.close()
            return
    except:
        print("Close")
        connection.close()


while True:
    print ("Waiting for connection")
    try:
        connection, address = sock.accept()
        _thread.start_new_thread(handle, (connection, address))
    except:
        sock.close()
        break
