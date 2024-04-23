import turtle

cherepaha = turtle.Turtle()
cherepaha.shape("turtle")
cherepaha.speed(100)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(12):
    cherepaha.color(colors[i % len(colors)])
    cherepaha.circle(100)
    cherepaha.right(30)
turtle.done()