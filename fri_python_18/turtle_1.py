import turtle
import time

list_colors = ['yellow', 'red', 'blue', 'white', 'pink']

t=turtle.Pen()

turtle.bgcolor('black')

t.pencolor(list_colors[0])

t.forward(100)

t.left(120)

t.pencolor(list_colors[1])

t.forward(100)

t.left(120)

t.pencolor(list_colors[3])

t.forward(100)

t.up()


t.forward(200)

t.down()

t.forward(100)

time.sleep(10000)
