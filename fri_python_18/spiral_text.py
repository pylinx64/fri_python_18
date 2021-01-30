import turtle

list_colors = ['#77818E', '#37DE53', '#DAFF2D', '#FF312D', '#D22DFF']
t = turtle.Pen()
turtle.bgcolor('black')

text = turtle.textinput('Подсказка 1', 'Подсказка 2')

for i in range(10000):
	t.pencolor(list_colors[i%5])
	t.penup()
	t.forward(i * 35)
	t.down()
	t.write(text, font=('Arial Bold', int((i + 4) / 4), 'bold'))
	t.left(72)
	
