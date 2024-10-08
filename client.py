# Echo client program
import socket
from InitTrackerClasses import creature

tracker:list = []

def connect():
    HOST = '127.0.0.1'
    PORT = 50007
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Connection established')
        return s

def RecieveLoop(s):
    while True:
        data = "b'greif1, enemy, 16, 23, 34';'greif2, enemy, 16, 32, 34'" #s.recv(1024)
        # print('Received', repr(data))
        tracker = []
        recieved = repr(data).removeprefix("b")
        for i in recieved.split(";"):
            creatureInfo = i.split(",")
            tracker.append(creature(player=bool(creatureInfo[0]),name=creatureInfo[1],tag=creatureInfo[2],initiative=creatureInfo[3],hp=int(creatureInfo[4]),maxhp=creatureInfo[5]))
        print(tracker)

print("connecting...")
connection = connect()
print("connected")
print("starting recieving loop")
RecieveLoop(connection)