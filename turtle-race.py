

import turtle
from random import randint as rn

t = turtle.Turtle()

t.speed(0)
t.penup()
t.goto(-60,200)
t.write('turtle race',font=('Verdana',20,'normal','underline'))
t.penup()
t.goto(-140,140)
for i in range(16):
	t.write(i,align='center')
	t.right(90)
	t.forward(10)
	t.pendown()
	t.forward(150)
	t.penup()
	t.backward(160)
	t.left(90)
	t.forward(20)

ada = turtle.Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

bob = turtle.Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()

dan = turtle.Turtle()
dan.color('green')
dan.shape('turtle')
dan.penup()
dan.goto(-160,40)
dan.pendown()

kat = turtle.Turtle()
kat.color('yellow')
kat.shape('turtle')
kat.penup()
kat.goto(-160,10)
kat.pendown()

for i in range(100):
	ada.forward(rn(1,5))
	bob.forward(rn(1,5))
	dan.forward(rn(1,5))
	kat.forward(rn(1,5))

turtle.done()
