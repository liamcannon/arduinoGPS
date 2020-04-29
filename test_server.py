import socket
import serial
import math

lastpoint = []

try:
    arduino = serial.Serial("/dev/cu.usbserial-DN040FPB", timeout = 10)
    print("Port Good")
except:
    print('Check Port')

def distance(x1, y1, x2, y2):
    d = math.sqrt(pow(2, (x2 - x1)) + pow(2, (y2 - y1)))
    return d

gettingData = True

sock = socket.socket()
sock.connect(("fuzytech.com", 47000))

while gettingData:
    rawdata = []

    for i in range(2):
        rawdata.append(arduino.readline().decode("utf-8"))
    print(rawdata)
    tmpPointsStr = rawdata[1].split(';')
    tmpPoints = [float(tmpPointsStr[0]), float(tmpPointsStr[1])]
    if(len(lastpoint) >= 2 and distance(rawdata[0], rawdata[1], lastpoint[0], lastpoint[1]) > .005 ):
        lastpoint[0] = tmpPoints[0]
        lastpoint[1] = tmpPoints[1]
        data = "data`"
        data += tmpPoints[0]+";"+tmpPoints[1]
        data += "`"
        data = data.encode('utf-8')

    elif len(lastpoint) < 2:
        lastpoint.append(tmpPoints[0])
        lastpoint.append(tmpPoints[1])
        data = "data`"
        #data += tmpPoints[0]+";"+tmpPoints[1]
        data += "`"
        data = data.encode('utf-8')
    data += 43.207008
    data += -70.774208
    print(data)
    sock.sendall(data)

sock.close()
