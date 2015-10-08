__author__ = 'jeroendevries'
def naam():
    global naam
    print("Wat is uw naam");naam=input()

def begin_station():
    global b_s
    print("Wat is uw begin station");b_s=input()

def eind_station():
    global e_s
    print("Wat is uw eindstation");e_s=input()
def beveilig_gegevens():
    gegevens = str(naam) + " " + str(b_s) + " " + str(e_s)
    global unieke_code, unieke_code1
    unieke_code = ""
    for x in gegevens:
        char_code = ord(x)+3
        unieke_code += chr(char_code)
    unieke_code1 = unieke_code[:20]
    print(gegevens)


naam()
begin_station()
eind_station()
beveilig_gegevens()
print(unieke_code1)
