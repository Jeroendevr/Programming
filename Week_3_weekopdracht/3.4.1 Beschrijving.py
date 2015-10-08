__author__ = 'jeroendevries'

def temperatuur(temp):
    if temp > 30:
        print("Vandaag veel water nodig")
    elif 20 < temp < 30:
        print("Vandaag veel thee nodig")
    else:
        print("Het wordt fris vandaag, veel chocolade ")

voorraad = {
    'mars':2,
    'snickers':2
}

def genoeg_voorraad():
    """
    x = gewenste voorraard
    :return:
    """
    x = 5
    for bar in voorraad:
        if voorraad[bar] < x:
            print(bar + " aanvullen met " + str(5-voorraad[bar]))


temp_a = input("Hoe warm wordt het vandaag? ")
while not temp_a.isnumeric():
    print("gast...")
    temp_a = input("Hoe warm wordt het vandaag? ")

temp_a = int(temp_a)
temperatuur(temp_a)

genoeg_voorraad()




