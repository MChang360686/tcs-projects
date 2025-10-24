import turtle

screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()

color = input("Please enter a color ")
t.color(color)
t.shape("turtle")

while True:
    direction = input("Please enter a direction to go ")

    match direction:
        case "u":
            t.setheading(90)
            steps = int(input("Please enter a distance in pixels "))
            t.forward(steps)
        case "l":
            t.setheading(180)
            steps = int(input("Please enter a distance in pixels "))
            t.forward(steps)
        case "d":
            t.setheading(270)
            steps = int(input("Please enter a distance in pixels "))
            t.forward(steps)
        case "r":
            t.setheading(0)
            steps = int(input("Please enter a distance in pixels "))
            t.forward(steps)


screen.mainloop()