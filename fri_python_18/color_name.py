import colorama
import random

from colorama import Fore

colorama.init()

colors = [Fore.GREEN, Fore.YELLOW, Fore.RED]

name = input()
# проверяет на тип данные
print(type(colors))

name = list(name)
#print(name)

name_1 = []
for i in name:
	i = Fore.RED + i + Fore.RESET
	name_1.append(i)
	print(name_1)
	
print(name)

