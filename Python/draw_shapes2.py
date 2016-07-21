# just drawing stuff on my own
# 07/06/2016

from turtle import *

def regular_polygon(sides, length, color):
	fillcolor(color)
	begin_fill()
	for i in range(sides):
		pencolor(color)
		pendown()
		speed(5)
		forward(length)
		left((360/int(sides)))
		penup()
	end_fill()
	forward(int(length) + 30)

penup()
goto(-200, 75)

regular_polygon(5, 70, "turquoise")
regular_polygon(12, 40, "steelblue")
regular_polygon(10, 50, "salmon")
regular_polygon(7, 60, "deepskyblue")

def repeat(sides, length, color):
	fillcolor(color)
	begin_fill()
	for i in range(sides):
		pencolor(color)
		pendown()
		speed(5)
		forward(length)
		left((360/int(sides)))
		penup()
	end_fill()
	forward(length)

goto(-215, -20)
for i in range(3):
	repeat(4, 50, "blue")
	repeat(4, 50, "red")
	repeat(4, 50, "yellow")

def houses(color):
	pencolor(color)
	pendown()
	fillcolor(color)
	begin_fill()
	forward(40)
	left(90)
	forward(30)
	left(45)
	forward(28)
	left(90)
	forward(28)
	left(45)
	forward(30)
	end_fill()
	penup()
	left(90)
	forward(40)

goto(-225, -100)	
for i in range(3):
	houses("dodgerblue")
	houses("mediumslateblue")
	houses("cyan3")
	houses("gold")
right(180)
for i in range(3):
	houses("dodgerblue")
	houses("mediumslateblue")
	houses("cyan3")
	houses("gold")

done()