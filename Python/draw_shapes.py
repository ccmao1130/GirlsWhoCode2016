# Draw Shapes
# 07/05/2016

'''
Some turtle functions you can use to make your shapes


forward(<distance>) - This function takes a positive or negative number and will move the turtle forward.

back(<distance>) - This function takes a positive or negative numbers and it will move the turtle back.

right(<angle>) - This function takes a number that represents angle in degrees. It will turn the turtle to  its right

left(<angle>) - This functions takes an number that represents an angle in degrees. It will turn the turtle to its left.

pencolor(<color>) - This functions takes a string that represents a color. The turtle's pen will draw in that color. The possible color values can be found at https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

penup() - This function takes no parameters. When called it will lift the turtle's pen up, the turtle will not draw when moved.

pendown() - This function takes no parameters. When called it will put the turtle's pen down. It will draw when moved.

speed(<number>) - This function takes a number. It determines how fast the turtle moves around the screen. Strangely enough if you want it to go as fast as possible you have to pass it 0 as a parameter.

goto(<x>, <y>) - This function takes two numbers, a position along the x-axis and a position along the y-axis. It will move the turtle to that position.

fillcolor(<color>) - This function takes a string that represents a color. The color will be used to fill shape the turtle has made. In order to get the turtle to fill the shape you have to use the begin_fill() function before the turtle starts drawing the shape and the end_fill() function after it finishes for the shape to be filled in.

begin_fill() - This function takes no parameters. It is put before the turtle draws a shape that you want filled in.

end_fill() - This function takes no parameters. It is put after the turtle has finished drawing a shape that you want filled in.

dot(<size>, <color>) - This function takes two parameters. The first is a positive number that represents the diameter of the dot to be drawn by the turtle. The second is a string that represents the color the dot should be.


BONUS:

circle(<radius>, <extent>, <steps>) - This function takes three parameters. However you only have to put in the first one. The <radius> parameter is the necessary parameter, it is a number that represents the radius of the circle. The <extent> is optional. It represents an angle saying how much of the circle should be drawn, if you don't put in anything for <extent> it will draw the whole circle. If you put in 180, it will draw a half circle. The third parameter <steps> is a number that represents how many steps the turtle should take to draw the circle. Try setting <steps> as 5 to see what happens.

'''

from turtle import *

# Part 1
# goes to starting location
penup()
side_length = 100
goto(-150,160)

# draws square
for i in range(4):
	pendown()
	speed(5)
	forward(side_length)
	left(90)
	penup()

# moves over so that the triangle is not drawn inside the square
forward(150)

# draws triangle
for i in range(3):
	pendown()
	speed(5)
	forward(side_length)
	left(120)
	penup()

# Part 2
# define function square so that you don't need to keep repeating the chunk of code
def square():
	for i in range(4):
		pendown()
		speed(5)
		forward(side_length)
		left(90)
		penup()

goto(-250,35)
for i in range(2):
	square()
	forward(110)

# define function triangle
def triangle():
	for i in range(3):
		pendown()
		speed(5)
		forward(side_length)
		left(120)
		penup()

goto(-10, 35)
for i in range(2):
	triangle()
	forward(110)
	
# Part 3
# drawing with colors
side_length2 = 50

# draws square with choice of color
def square2(color):
	for i in range(4):
		pencolor(color)
		pendown()
		speed(5)
		forward(side_length2)
		left(90)
		penup()

goto(-210, -40) # go to starting place
square2("red") # need to put color in quotes
forward(60)
square2("blue")
forward(60)
square2("green")

# draws triangle with choice of color
def triangle(color):
	for i in range(3):
		pencolor(color)
		pendown()
		speed(5)
		forward(side_length2)
		left(120)
		penup()

goto(-10, -40) # go to starting place
triangle("red")
forward(60)
triangle("blue")
forward(60)
triangle("green")

# draws any regular polygon with choice of # of sides, length of each side, and color of shape
def regular_polygon(sides, length, color):
	for i in range(sides):
		pencolor(color)
		pendown()
		speed(5)
		forward(length)
		left((360/int(sides)))
		penup()

goto(-200, -160) # go to starting place
regular_polygon(5, 50, "medium aquamarine") # pentagon
forward(80)
regular_polygon(6, 50, "blue violet") # hexagon
forward(80)
regular_polygon(10, 30, "LimeGreen") # decagon
forward(80)
regular_polygon(100, 5, "red")

goto(-200, -225)
for i in range(20): # repeating and overlapping shape
	regular_polygon(5, 20, "maroon")
	forward(2)
	
done() # to stop graphics window from closing after program is done executing
