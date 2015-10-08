__author__ = 'jeroendevries'

import turtle
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")

zijde = 50
schuine_zijde = 71
t.pendown()
t.left(90)
t.forward(zijde)
t.right(45)
t.forward(schuine_zijde/2)
t.right(90)
t.forward(schuine_zijde/2)
t.right(135)
t.forward(zijde)
t.left(135)
t.forward(schuine_zijde)
#rechter muur
t.left(135)
t.forward(zijde)
t.left(135)
t.forward(schuine_zijde)
#bodem
t.left(135)
t.forward(zijde)
#positioneren
t.penup()
t.right(180)
t.forward(zijde/2)
t.right(90)
t.forward(10)





turtle.mainloop()