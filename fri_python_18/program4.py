'''
try:
	x = input('Введите число: ')
	print(int(x) * 10)
except:
	print('Введите число правильно!')
'''
import colorama, random
from colorama import Fore
colorama.init()

print(Fore.GREEN + 'Hello world')

name = ['A', 'l', 'e', 'x']
colors = [Fore.WHITE, Fore.GREEN, Fore.RED, Fore.CYAN]
for z in name:
	print(random.choice(colors) + z, end='')

