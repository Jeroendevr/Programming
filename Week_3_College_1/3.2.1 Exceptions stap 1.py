__author__ = 'jeroendevries'
bedrag = 4356
def mensen():
    global men
    print("Hoeveel mensen gaan er mee?");men = input()

def kosten_pp(n):
    """
    Berekent de kosten pp
    :arg :De hoeveelheid mensen
    :return:
        Kosten pp
    """

    if int(men) == 0:
        print("Delen door 0 mag niet!")
    else:
        try:
            kosten = bedrag / int(men)
            return kosten
        except:
            print("Onverwachte fout")

mensen()
print(kosten_pp(men))