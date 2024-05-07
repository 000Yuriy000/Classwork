import turtle

screen = turtle.Screen()
screen.title("my title")

cherepaha = turtle.Turtle()
cherepaha.color("black")
cherepaha.shape("turtle")

def draw_arc(turtle, radius, angle):
    for _ in range(angle):
        turtle.forward(radius)
        turtle.right(1)

side_length = 100
corner_radius = 2

for _ in range(4):
    cherepaha.forward(side_length - corner_radius)
    draw_arc(cherepaha, corner_radius, 90)

text = ">>>>Hello World!"
cherepaha.penup()
cherepaha.goto(-20,-100)
cherepaha.write(text, align="center",
font=("Arial", 12, "normal"))

turtle.done()