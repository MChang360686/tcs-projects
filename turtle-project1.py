import turtle

screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()

shape = input("Please enter a shape name")
color =  input("Please enter a color")
size = int(input("Please enter a number of pixels"))

def drawShape(shape, color, size):
    if shape == "circle":
        t.color(color)
        t.circle(size)
    elif shape == "square":
        t.color(color)
        for i in range(0, 4):
            t.forward(size)
            t.right(90)
    elif shape == "triangle":
        t.color(color)
        for i in range(0, 3):
            t.forward(size)
            t.left(120)
    elif shape == "pentagon":
        t.color(color)
        for i in range(0, 5):
            t.forward(size)
            t.left(72)
    else:
        print("I don't know that shape")


drawShape(shape, color, size)
t.screen.mainloop()