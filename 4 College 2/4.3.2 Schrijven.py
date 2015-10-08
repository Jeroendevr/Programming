__author__ = 'jeroendevries'
import csv


def reiziger():
    bestand = open('mensen.csv', 'w')
    reader = csv.DictWriter(bestand, delimiter=',', fieldnames=['Voorletter(s)', 'Achternaam', 'Geboortedatum','E-Mailadres'])
    voorletter = input("Wat zijn je voorletters? \n")
    achternaam = input("Wat is je achternaam? \n")
    geboorte = input("Wat is je geboortedatum? \n")
    mail = input("Wat is je mailadres? \n")

    reader.writerow({'Voorletter(s)': voorletter, 'Achternaam': achternaam, 'Geboortedatum': geboorte,
                     'E-Mailadres': mail})

reiziger()