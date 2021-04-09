import socket
from datetime import datetime
import colorama

from colorama import Fore
colorama.init()

clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('26.194.184.205', 11719))                        # для общаги 192.168.1.132, 11719

quit = False
print("[Server Started]")

while not quit:
    try:
        data, addr = s.recvfrom(1024)
        '''
        if "26.129.95.168" == addr[0]:
            s.sendto('BAN'.encode("utf-8"), addr)
            continue
        '''

        if addr not in clients:
            clients.append(addr)
            
        
        server_time = datetime.strftime(datetime.now(), "%Y-%m-%d-%H.%M.%S")

        print("["+addr[0]+"]=["+str(addr[1])+"]=["+server_time+"]/",end="")
        print(data.decode("utf-8"))

        for client in clients:
            s.sendto(data,client)
    except:
        for client in clients:
            s.sendto('Server Stop'.encode("utf-8"), client)
        print("\n[Server Stopped]")
        quit = True

s.close()
