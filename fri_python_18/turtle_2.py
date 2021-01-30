import turtle
import time

list_colors = ['yellow', 'red', 'blue', 'white', 'pink']
t=turtle.Pen()

def side():
	'''Функция рисует сторону'''
	t.pencolor(list_colors[1])
	t.forward(10)
	t.left(5)
	
i = 0
while i < 72:
	side()
	i += 1
	
time.sleep(1000)
