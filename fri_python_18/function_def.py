import turtle

colors=['#FF0000', '#1EFF00', '#00DDFF']

turtle.bgcolor('black')

t=turtle.Pen()
t.shape('turtle')


def side(angle, lenth, number):
	t.pencolor(colors[number])
	t.forward(lenth)
	t.left(angle)

while True:
	side(49, 100, 1)
	side(145, 100, 0)
	side(227, 100, 2)

turtle.done()
