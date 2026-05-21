import turtle as t
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
t.speed(0)  # Fastest drawing speed
for x in range(360):
    t.pencolor(colors[x % 6])
    t.forward(x / 100 + 1)
    t.left(59)
    t.rt(90);