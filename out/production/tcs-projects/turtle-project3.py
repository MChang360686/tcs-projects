import turtle
import colorsys


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n = 70
h = 0


for i in range(0, 360):
    color = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(color)
    t.left(1)
    t.fd(1)
    for j in range(0, 2):
        t.left(2)
        t.circle(100)