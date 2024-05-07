import turtle

screen = turtle.Screen()
screen.title("my title")


cherepaha = turtle.Turtle()
cherepaha2 = turtle.Turtle()
cherepaha.speed(20)
cherepaha2.speed(20)
cherepaha.shape("turtle")
cherepaha2.shape("turtle")

cherepaha.color("green")
cherepaha2.color("red")
cherepaha2.left(180),

for _ in range(180):
    cherepaha.forward(2)
    cherepaha.left(1)
    cherepaha2.forward(2)
    cherepaha2.left(-1)

cherepaha.penup()


for _ in range(90):
    cherepaha.forward(-2)
    cherepaha.left(-1)

cherepaha.pendown()
cherepaha.right(-90)
cherepaha.forward(230)


cherepaha2.right(-90)
cherepaha2.forward(-230)

turtle.done()