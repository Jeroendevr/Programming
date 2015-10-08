__author__ = 'jeroendevries'
import turtle
import numpy as np
t = turtle.Turtle()
t.screen.bgcolor("yellow")
t.right(90)
t.pencolor("blue")
def welkom():
    t.write("Welkom bij de NS",font=("Arial",14,"normal"))
    t.forward(20)
    t.write("Hier is uw rapport:",font=("Arial",14,"normal"))
    t.forward(40)

def beginstation():
    t.write("Het beginstation Alkmaar is het 3e station in het traject?",font=("Arial",14,"normal"))
    t.forward(40)

def gem_reisagstand():
    gemiddelde = np.average(ritten)
    t.write("De gemiddelde reisafstand is " + str(gemiddelde) + " km",font=("Arial",14,"normal"))
    t.forward(40)

def mediaan():
    mediaan = np.median(ritten)
    t.write("De mediaan is " + str(mediaan),font=("Arial",14,"normal"))
    t.forward(40)

def minimaal():
    min = np.min(ritten)
    t.write("De minimale reisafstand is :" + str(min),font=("Arial",14,"normal"))
    t.forward(40)

def maximaal():
    maks = np.max(ritten)
    t.write("De maximale reisafstand is :" + str(maks),font=("Arial",14,"normal"))
    t.forward(40)

trein_traject = ["Schagen", "Huurhugowaard","Alkmaar","Castricum","Zaandam","Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel","Utrech Centraal","\'s Herthogenbosch","Eindhoven","Weert","Roermond","Sittard","Maastricht" ]

rit_prijs = 5

ritten=(11, 1, 3, 6, 4, 6, 8, 3, 5)

welkom()
gem_reisagstand()
mediaan()
minimaal()
maximaal()

turtle.mainloop()