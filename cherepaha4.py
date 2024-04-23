import turtle

screen = turtle.Screen()
screen.title("my title")
screen.bgcolor("black")


cherepaha = turtle.Turtle()
cherepaha.shape("turtle")
cherepaha.color("white")
a = 100
b = 50
cherepaha.speed(1)

cherepaha.forward(50)
cherepaha.circle(100, 180)
cherepaha.forward(50)
cherepaha.circle(100, 180)

turtle.done()