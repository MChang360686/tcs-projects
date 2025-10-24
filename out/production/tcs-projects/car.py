import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)  # Center of the circle
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_car():
    # Car body
    draw_rectangle("red", -100, -20, 200, 50)

    # Car top
    draw_rectangle("darkred", -70, 30, 140, 40)

    # Windows
    draw_rectangle("lightblue", -60, 40, 30, 25)
    draw_rectangle("lightblue", 10, 40, 30, 25)

    # Headlights
    draw_circle("yellow", -105, 5, 5)
    draw_circle("yellow", 105, 5, 5)

    # Wheels
    draw_circle("black", -60, -20, 20)
    draw_circle("black", 60, -20, 20)

def draw_road():
    draw_rectangle("gray", -300, -40, 600, 40)
    # Lane divider lines
    turtle.pensize(2)
    turtle.pencolor("white")
    for x in range(-250, 300, 60):
        draw_rectangle("white", x, -22, 30, 4)

def draw_sun():
    draw_circle("yellow", 200, 150, 40)

def main():
    turtle.speed(0)
    turtle.bgcolor("skyblue")
    draw_road()
    draw_car()
    draw_sun()
    turtle.hideturtle()
    turtle.done()

main()
