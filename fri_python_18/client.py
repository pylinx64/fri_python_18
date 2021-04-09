# -*- coding: utf-8 -*-

import time, socket, threading, colorama, random
from colorama import Fore
colorama.init()

def receving(name, sock, switch):
	while not switch:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				print('\n'+data.decode("utf-8"))
				time.sleep(0.2)
		except:
			pass


# Выкл; подключение 	
shutdown = False
join = False

# ваш ip  и порт
host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("26.194.184.205", 11719)

# подключаемся к серверу
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

name = input("$ name: ")
colors = [Fore.GREEN, Fore.RED, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA]
name = list(name)
name = [random.choice(colors)+char for char in name]
name = ''.join(name)

# отправляет сообщения 
s.sendto(("["+Fore.CYAN+name+Fore.RESET+"] => join chat ").encode("utf-8"), server)
time.sleep(0.2)

rT = threading.Thread(target = receving, args = ("RecvThread", s, shutdown))
rT.start()

while shutdown == False:
	try:
		message = input("["+name+"] > ")
		if message != "":
			s.sendto(("["+name+"] > "+Fore.YELLOW+message+Fore.RESET).encode("utf-8"), server)
		time.sleep(0.2)
	except:
		s.sendto(("["+Fore.CYAN+name+Fore.RESET+"] <= left chat ").encode("utf-8"), server)
		shutdown = True

rT.join()		
s.close()
