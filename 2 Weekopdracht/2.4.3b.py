__author__ = 'jeroendevries'
def naam():
    naam=input("Wat is uw naam: ")
    return naam

def begin_station():
    b_s = input("Wat is uw begin station")
    return b_s

def eind_station():
    e_s = input("Wat is uw eindstation")
    return e_s

def beveilig_gegevens(a,b,c):
    gegevens = str(a) + " " + str(b) + " " + str(c)
    global unieke_code, unieke_code1
    unieke_code = ""
    for x in gegevens:
        char_code = ord(x)+3
        unieke_code += chr(char_code)
    unieke_code1 = unieke_code[:20]
    print(gegevens)


naam = naam()
begin = begin_station()
eind = eind_station()
beveilig_gegevens(naam, begin, eind)
print(unieke_code1)

