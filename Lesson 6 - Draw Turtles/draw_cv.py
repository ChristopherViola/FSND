import turtle

def draw_initials():
    window = turtle.Screen()
    window.bgcolor("purple")
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("yellow")
    pen.speed(3)

    #draw C
    for i in range(1,4):
        pen.back(100)
        pen.left(90)

    pen.pu()
    pen.setpos(10,0)
    pen.pd()

    #draw V
    pen.goto(60,-100)
    pen.goto(110,0)

    window.exitonclick()

draw_initials()
