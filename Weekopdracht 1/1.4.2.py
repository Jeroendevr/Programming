__author__ = 'jeroendevries'
import turtle
import numpy as np


# t = turtle.Turtle()
# t.screen.bgcolor("yellow")
# turtle.mainloop()
def welkom():
    print("Welkom bij de NS")
    print("Hier zijn uw reisgegevens:")

def beginstation():
    print("Beginstation?")
    b_station = input()
    return b_station

def eindstation():
    print("Eindstation?")
    e_station = input()
    return e_station

def ritprijs(b,e):
    stations = trein_traject.index(e) - trein_traject.index(b)
    prijs = 5* stations
    return prijs


trein_traject = ["Schagen", "Huurhugowaard","Alkmaar","Castricum","Zaandam","Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel","Utrech Centraal","\'s Herthogenbosch","Eindhoven","Weert","Roermond","Sittard","Maastricht" ]


welkom()
begin = beginstation()
eind = eindstation()
print(ritprijs(begin,eind))

