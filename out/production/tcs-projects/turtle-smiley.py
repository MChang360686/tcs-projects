import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_smiley_face():
    screen = turtle.Screen()
    screen.bgcolor("white")
    turtle.speed(5)

    draw_circle("yellow", 0, 0, 100)

    draw_circle("black", -40, 50, 10)

    draw_circle("black", 40, 50, 10)

    turtle.penup()
    turtle.goto(-50, -20)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.pensize(5)
    turtle.circle(60, 120)

    turtle.hideturtle()
    screen.mainloop()

draw_smiley_face()
