__author__ = 'jeroendevries'

import random
def dobbelsteen(min=1, max=6):
    """ Geeft tussen twee waarden
    Args
    min = minimale waarde
    max: de maximale waarde
    Return:
        Een getal russen min en max
    """
    x=random.randrange(min,max+1)
    return x

z=dobbelsteen()
print("Random waarde:",z)
z=dobbelsteen(max=10)
print("Random waarde:",z)
