import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
t = turtle.Turtle()
t.speed(3)

# Helper function to draw a filled circle
def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw face
draw_circle(0, 0, 100, "yellow")

# Draw eyes (under glasses)
draw_circle(-35, 40, 10, "white")
draw_circle(35, 40, 10, "white")
draw_circle(-35, 40, 5, "black")
draw_circle(35, 40, 5, "black")

# Draw glasses lenses
draw_circle(-35, 40, 20, "black")
draw_circle(35, 40, 20, "black")

# Draw glasses bridge
t.penup()
t.goto(-15, 40)
t.pendown()
t.width(5)
t.goto(15, 40)

# Draw flat mouth
t.penup()
t.goto(-30, -40)
t.setheading(0)
t.width(5)
t.pendown()
t.forward(60)

# Hide turtle
t.hideturtle()

# Keep the window open
screen.mainloop()