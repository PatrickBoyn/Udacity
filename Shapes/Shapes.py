import turtle

# variables
window = turtle.Screen()
brad = turtle.Turtle()

# changes the screen color and shape of the turtle
# it also changes the speed of the drawing
brad.shape("turtle")
brad.color("green")
window.bgcolor("grey")
brad.speed(3)

def draw_square():

	# loops and creates a square
	for i in range(4):
		brad.forward(100)
		brad.right(90)
	# End of function

def draw_circle():

	# defines a radius of x ammount
	brad.circle(100)
	# End of function

def draw_triangle():

	brad.left(60)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(135)
	brad.forward(130)
	
	window.exitonclick()
	# End of function

draw_square()






