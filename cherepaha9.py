import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)

screen.bgpic('S:\\Группы\\ИБС235 Алгоритмизация\\II семестр\\Задание 8. Turtle\\back1.PNG')

cherepaha = turtle.Turtle()
cherepaha.shape("turtle")

def moce():
    cherepaha.forward(50)
for i in range(6):
    for j in range(6):
        if (i + j) % 2 == 0:
            moce()
        else:
            cherepaha.penup()
            moce()
            cherepaha.pendown()

turtle.done()