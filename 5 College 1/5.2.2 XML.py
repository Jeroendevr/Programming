__author__ = 'jeroendevries'

import xmltodict

def verwerk_xml():
    bestand = open('perrons.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

stations_dict = verwerk_xml()
print(stations_dict['perrons']['perron'][2])