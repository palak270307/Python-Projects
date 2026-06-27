import turtle
import random

t = turtle.Turtle()
t.speed(0)         # Fastest drawing speed
turtle.bgcolor("black")

colors = ["red", "pink", "yellow", "purple", "cyan", "orange", "white"]

def draw_heart():
    t.color(random.choice(colors))
    t.begin_fill()
    
    t.left(140)
    t.forward(120)
    t.circle(-60, 200)
    t.left(120)
    t.circle(-60, 200)
    t.forward(120)
    
    t.end_fill()

# Continuous loop
while True:
    t.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    t.pendown()
    
    t.setheading(0)  # Reset direction
    draw_heart()
