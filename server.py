import socket
from InitTrackerClasses import creature

tracker:list = []

def Action(request, client):
    request = request.split(" ")
    match request[0]:
        case "add":
            tracker.append(creature(name=request[1],type=request[2],initiative=request[3],hp=request[4],maxhp=request[5]))
        case "remove":
            for i in tracker:
                if i.name == request[1]:
                    tracker.remove(i)
        case "damagebyname":
            for i in tracker:
                if i.name == request[1]:
                    i.hp = int(i.hp)
                    i.hp -= int(request[2])
        case "damagebytype":
            for i in tracker:
                if i.type == request[1]:
                    i.hp = int(i.hp)
                    i.hp -= int(request[2])
        case _:
            print("try again")
    stringToSend:str = ""
    for i in tracker:
        print(i)
        stringToSend += (str(i)+";")
    bytesToSend = stringToSend.encode('utf-8')
    client.sendall(bytesToSend)

HOST = '192.168.178.39'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        print("add name type init hp maxhp")
        print("remove name")
        print("damage name amount")
        while True:
            Action(input(), conn)
            # data = conn.recv(1024)
            # if not data: continue
            # print(data)