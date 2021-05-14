# -*- coding: utf-8 -*-

import socket, colorama, time, threading
from colorama import Fore, Style
import random

colorama.init()

def receving (name, sock, switch):
	while not switch:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				print(' '+data.decode("utf-8"))
				time.sleep(0.2)
		except:
			pass     

# Выкл, подключение
shutdown = False
join = False

# host - ip комп
host = socket.gethostbyname(socket.gethostname())
port = 0

# ip и порт сервера
server = ("192.168.31.43", 11721)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

name = input("$ name: ")

colors = [Fore.GREEN, Fore.RED, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA]
name = list(name)
name = [random.choice(colors)+char for char in name]
name.extend(Fore.RESET)
name = ''.join(name)
s.sendto(("["+name+"] => join chat ").encode("utf-8"), server)
time.sleep(0.2)

rT = threading.Thread(target = receving, args = ("RecvThread", s, shutdown))
rT.start()

while shutdown == False:
	try:
		print("["+name+"] > ", end='')
		print(Fore.GREEN, end='')
		message = input()
		message = Fore.GREEN+message+Fore.RESET
		print(Fore.RESET, end='')
		if message != "":
			s.sendto(("["+name+"] > "+message).encode("utf-8"), server)
		time.sleep(0.2)
	except:
		s.sendto(("["+name+"] <= left chat ").encode("utf-8"), server)
		shutdown = True
	
rT.join()
s.close()
