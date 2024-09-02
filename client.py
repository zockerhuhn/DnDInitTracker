# Echo client program
import socket

class creature:
    def __init__(self, name, type, ac:int, hp:int, maxhp:int):
        self.name = name
        self.type = type
        self.ac:int = ac
        self.hp:int = hp
        self.maxhp:int = maxhp
    def __str__(self):
        return f"{self.name}, {self.type}, {self.ac}, {self.hp}, {self.maxhp}"


HOST = '192.168.178.39'     # The remote host
PORT = 50007                # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Connection established')
    while True:
        data = s.recv(1024)
        print('Received', repr(data))