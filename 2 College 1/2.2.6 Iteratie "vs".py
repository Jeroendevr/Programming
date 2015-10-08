__author__ = 'jeroendevries'
traject = ["Woerden","Vleuten","Utrecht Terwijde","Utrecht Leidsche Rijn", "Utrecht Centraal"]
huidig_station = "Woerden"

while traject.index(huidig_station)+1 < len(traject):
    x = traject.index(huidig_station) + 1
    huidig_station = traject[x]
    print(huidig_station)
