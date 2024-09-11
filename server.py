import socket
from InitTrackerClasses import creature

tracker:list = []

skipConnect = True

def Action(request, client):
    request = request.split(" ")
    match request[0]:
        case "add":
            tracker.append(creature(player=bool(request[1]),name=request[2],tag=request[3],initiative=request[4],hp=int(request[5]),maxhp=request[6]))
        case "remove":
            for i in tracker:
                if i.name == request[1]:
                    tracker.remove(i)
        case "damagebyname":
            for i in tracker:
                if i.name == request[1]:
                    i.hp -= int(request[2])
        case "damagebytag":
            for i in tracker:
                if i.tag == request[1]:
                    i.hp -= int(request[2])
        case _:
            print("try again")
    stringToSend:str = ""
    for i in tracker:
        print(i)
        stringToSend += (str(i)+";")
    if not skipConnect:
        client.sendall(stringToSend.encode('utf-8'))

def connect():
    HOST = ''
    PORT = 50007
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
    return conn

while 1:
    if not skipConnect:
        conn = connect()
    else:
        conn = None
    print("add player name tag init hp maxhp \n remove name \n damagebyname name amount \n damagebytag tag amount")
    while True:
        Action(input(), conn)