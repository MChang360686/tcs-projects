import turtle

screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()

"""for color in ["red", "green", "blue", "yellow"]:
    t.color(color)
    t.forward(50)
    t.right(90)

t.fillcolor("red")
t.begin_fill()



radius = 20
t.circle(radius)

for i in range(0, 3):
    t.forward(100)
    t.left(120)"""

shape = input("Please enter a shape name")
color =  input("Please enter a color")
size = int(input("Please enter a number of pixels"))

def drawShape(shape, color):
    if shape == "circle":
        t.color(color)
        t.circle(100)
    elif shape == "square":
        t.color(color)
        for i in range(0, 4):
            t.forward(100)
            t.right(90)
    elif shape == "triangle":
        t.color(color)
        for i in range(0, 3):
            t.forward(100)
            t.left(120)
    elif shape == "pentagon":
        t.color(color)
        for i in range(0, 5):
            t.forward(100)
            t.left(72)
    else:
        print("I don't know that shape")


drawShape(shape, color)
t.screen.mainloop()

"""shape = input("Please enter a shape name ")
color = input("Please enter a color ")

v = turtle.getscreen()
t = turtle.Turtle()

t.color(color)

if shape == "square":
    for x in range(4):
        t.forward(10)
        t.right(90)
        x += 1"""