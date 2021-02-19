# -*- coding: utf-8 -*-

import socket, colorama, time, threading


def receving (name, sock, switch):
	while not switch:
		try:
			while True:
                data, addr = sock.recvfrom(1024)
                print('\n'+data.decode("utf-8"))
                time.sleep(0.2)
		except:
			pass     


