__author__ = 'jeroendevries'
import turtle
t = turtle.Turtle()
t.screen.bgcolor("yellow")
t.pencolor("blue")
font = (("Arial",14,"normal"))
def welkom():
    b= 300
    h = 50
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
    t.write("Het beginstation Alkmaar is het 3e station in het traject?",font=font)
    t.forward(40)

def eindstation():
    t.write("Het eindstation Weert is het 12e station in het traject.",font=font)
    t.forward(40)

def afstand():
    t.write("De afstand bedraagt 9 stations.",font=font)
    t.forward(40)

def prijs():
    t.write("De prijs van het kaartje is 45 euro",font=font)
    t.forward(40)

trein_traject = ["Schagen", "Huurhugowaard","Alkmaar","Castricum","Zaandam","Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel","Utrech Centraal","\'s Herthogenbosch","Eindhoven","Weert","Roermond","Sittard","Maastricht" ]

rit_prijs = 5
welkom()
beginstation()
eindstation()
afstand()
prijs()
turtle.mainloop()