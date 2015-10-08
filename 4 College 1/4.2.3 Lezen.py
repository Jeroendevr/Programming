__author__ = 'jeroendevries'
def bestand():
    try:
        file = open('lezenvanfiles.txt','r')
    except:
        print("Kon het bestand niet vinden")

    for x in file:
        OV,naam = x.split(',')
        print("OV-nummer: "+ OV + " is van " + naam )
    file.close()

bestand()