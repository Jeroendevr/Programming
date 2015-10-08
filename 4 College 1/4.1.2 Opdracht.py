__author__ = 'jeroendevries'
import random
def select_winner(persons):
    """Select a random item from a given list"""
    print("De winnaar wordt gekozen uit de volgende lijst:")
    for person in persons:
        print(person, end=' ')
    print()
    return random.choice(persons)

namen = ["Jan","Piet","Klaas","Greet","Koen","Ahmed","Yzdril","Jeroen"]

def naam():
    global nieuwe_naam
    print("Voor een naam in"); nieuwe_naam = input()
    while nieuwe_naam == "":
        print("Voor een naam in"); nieuwe_naam = input()
    namen.append(nieuwe_naam)

naam()
namen.sort()
winnaar = select_winner(namen)
if winnaar == nieuwe_naam:
    print("U heeft een gratis ov-jaarkaart  gewonnen")
else:
    print("Helaas u heeft niet gewonnen de winnaar is "+ winnaar)