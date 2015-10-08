__author__ = 'jeroendevries'
import datetime
today = datetime.datetime.today()

def aankomst():
    naam = input("Wie is er nu in Groningen aangekomen")
    bestand = open('resultaat.txt','a')
    s = today.strftime("%a %d %b %Y, %H:%M:%S")
    bestand.write(naam + " "+ s + '\n')
    bestand.close()

aankomst()
aankomst()
