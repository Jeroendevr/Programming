__author__ = 'jeroendevries'
import csv


bestand = open('lezen.csv', 'r')


def lezen():

    try:
        reader = csv.DictReader(bestand, delimiter=';')
        for row in reader:
            if int(row['Snelheid (km/u)']) <= 140:
                print(' {0:40s} - {1:3s} '.format(row['Baanvak'],row['Snelheid (km/u)']))
    finally:
        bestand.close()

lezen()