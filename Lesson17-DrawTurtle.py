import turtle

def draw_square(angle):
	# window = turtle.Screen()
	# window.bgcolor("blue")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(50)
	line = 0
	brad.right(angle)
	while line < 4:
		brad.forward(100)
		brad.right(90)
		line += 1
	# window.exitonclick()

def draw_circle():
	angie = turtle.Turtle()
	angie.color("white")
	angie.shape("arrow")
	angie.circle(100)
	angie.speed(10)
	# window.exitonclick()

def draw_triangle(angle):
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(50)
	line = 0
	brad.right(angle)
	while line < 3:
		brad.forward(100)
		brad.right(120)
		line += 1
	# window.exitonclick()

def draw_square_circle():
	window = turtle.Screen()
	window.bgcolor("red")

	count = 40
	angle = 360/count
	index = 0
	while index < count:
		draw_square(index * angle)
		index += 1
	window.exitonclick()

def draw_triangle_circle():
	window = turtle.Screen()
	window.bgcolor("white")

	count = 40
	angle = 360/count
	index = 0
	while index < count:
		draw_triangle(index * angle)
		index += 1
	window.exitonclick()

# draw_square(0)
# draw_circle()
# draw_triangle()
# draw_square_circle()
draw_triangle_circle()
	