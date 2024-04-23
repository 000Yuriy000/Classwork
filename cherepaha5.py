import turtle

cherepaha = turtle.Turtle()
cherepaha.shape("turtle")
cherepaha.fillcolor("red")
cherepaha.pencolor("red")

cherepaha.begin_fill( )
for _ in range(6):
    cherepaha.forward(100)
    cherepaha.right(144)

cherepaha.end_fill()
turtle.done()
