__author__ = 'jeroendevries'
traject = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]

import turtle
t = turtle.Turtle()
t.screen.bgcolor("yellow")
t.pencolor("blue")
font = (("Arial",14,"normal"))
b_s = ""
e_s = ""

def welkom():
    b= 300
    h = 50
    t.pu()
    t.left(180)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.pd()
    t.forward(b)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(h)
    t.up()
    t.right(90)
    #begin positie tekst
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.write("Welkom bij de NS",font=font)
    t.forward(20)
    t.write("Hier zijn uw reisgegevens:",font=font)
    #Einde welkom cursor positioneren
    t.right(90)
    t.forward(2*h)
    t.left(90)
    t.forward(h)

def beginstation():
    global b_s
    while b_s not in traject:
        t.write("Geef het beginstation op",font=font);b_s = input()
        t.forward(20)
    t.write("Het begin station is " + b_s, font=font)
    t.forward(20)

def eindstation():
    global e_s
    while e_s not in traject:
        t.write("Geef het eindstation op",font=font);e_s = input()
        t.forward(20)
    t.write("Het eindstation is " + e_s, font=font)
    t.forward(20)

def

def afstand():
    t.write("De afstand bedraagt 9 stations.",font=font)
    t.forward(40)

def prijs():
    t.write("De prijs van het kaartje is 45 euro",font=font)
    t.forward(40)
def reis():
    t.write("Het begin station is " + b_s + " en het eindstation is " + e_s, font= font)

trein_traject = ["Schagen", "Huurhugowaard","Alkmaar","Castricum","Zaandam","Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel","Utrech Centraal","\'s Herthogenbosch","Eindhoven","Weert","Roermond","Sittard","Maastricht" ]

rit_prijs = 5
welkom()
#beginstation()
#eindstation()
#afstand()
#prijs()

reis()
turtle.mainloop()