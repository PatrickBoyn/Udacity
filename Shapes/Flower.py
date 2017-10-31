import turtle

window = turtle.Screen()
triangle = turtle.Turtle()

triangle.shape('classic')
triangle.color('blue' , 'red')
window.bgcolor('lightblue')


def draw_triangle():
	triangle.goto(0,100)
	triangle.forward(100)
	triangle.right(135)
	triangle.forward(140)
	triangle.begin_fill()
	
for i in range(37):
	draw_triangle()
	triangle.right(10)
	triangle.end_fill()



window.exitonclick()