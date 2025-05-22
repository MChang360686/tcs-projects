import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

boat = turtle.Turtle()
boat.speed(3)

def draw_ocean():
    boat.penup()
    boat.goto(-400, -200)
    boat.color("darkblue")
    boat.begin_fill()
    boat.pendown()
    for _ in range(2):
        boat.forward(800)
        boat.right(90)
        boat.forward(200)
        boat.right(90)
    boat.end_fill()
    boat.penup()

def draw_hull():
    boat.penup()
    boat.goto(-100, -150)
    boat.setheading(0)
    boat.color("saddlebrown")
    boat.begin_fill()
    boat.pendown()
    boat.goto(100, -150)
    boat.goto(70, -200)
    boat.goto(-70, -200)
    boat.goto(-100, -150)
    boat.end_fill()
    boat.penup()

def draw_sail():

    boat.goto(0, 50)
    boat.color("white")
    boat.begin_fill()
    boat.pendown()
    boat.goto(100, -50)
    boat.goto(0, -50)
    boat.goto(0, 50)
    boat.end_fill()
    boat.penup()

    boat.goto(0, 50)
    boat.begin_fill()
    boat.pendown()
    boat.goto(-100, -50)
    boat.goto(0, -50)
    boat.goto(0, 50)
    boat.end_fill()
    boat.penup()

def draw_mast():
    boat.goto(0, -150)
    boat.setheading(90)
    boat.color("black")
    boat.pensize(10)
    boat.pendown()
    boat.forward(200)
    boat.penup()
    boat.pensize(1)

def draw_sun():
    boat.goto(150, 150)
    boat.color("yellow")
    boat.begin_fill()
    boat.pendown()
    boat.circle(40)
    boat.end_fill()
    boat.penup()

def draw_cloud(x, y):
    boat.goto(x, y)
    boat.color("white")
    boat.begin_fill()
    for _ in range(3):
        boat.circle(20)
        boat.goto(boat.xcor() + 20, boat.ycor())
    boat.end_fill()
    boat.penup()

def draw_bird(x, y):
    boat.goto(x, y)
    boat.color("black")
    boat.setheading(60)
    boat.pendown()
    boat.circle(-10, 60)
    boat.left(120)
    boat.circle(-10, 60)
    boat.penup()
    boat.setheading(0)

draw_ocean()
draw_hull()
draw_sail()
draw_mast()  
draw_sun()

draw_cloud(-200, 180)
draw_cloud(-100, 160)
draw_cloud(50, 190)

draw_bird(-50, 100)
draw_bird(0, 120)
draw_bird(60, 110)

boat.hideturtle()
screen.mainloop()
