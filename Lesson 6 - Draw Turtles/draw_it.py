import turtle

def draw_square():
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("blue")
    pen.speed(3)
    i = 0
    while (i < 4):
        pen.forward(100)
        pen.right(90)
        i = i + 1

def draw_circle():
    pen = turtle.Turtle()
    pen.shape("arrow")
    pen.color("red")
    pen.speed(2)
    pen.circle(100)
    

def draw_triangle():
    pen = turtle.Turtle()
    pen.shape("circle")
    pen.color("yellow")
    pen.speed(4)
    i = 0
    while (i < 3):
        pen.backward(100)
        pen.left(120)
        i = i + 1

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("green")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()

draw_shapes()
