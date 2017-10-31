import turtle

# variables
window = turtle.Screen()
brad = turtle.Turtle()

# changes the screen color and shape of the turtle
# it also changes the speed of the drawing
brad.shape("turtle")
brad.color("red")
window.bgcolor("darkblue")
brad.speed(3)

def draw_square():

	# loops and creates a square
	for i in range(4):
		brad.forward(100)
		brad.right(90)
	# End of function


for i in range(37):
	draw_square()
	brad.right(10)
	
window.exitonclick()
