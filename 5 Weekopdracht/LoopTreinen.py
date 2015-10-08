__author__ = 'jeroendevries'
import xmltodict


def stations():
    page = open('nstrein21.xml', 'r')
    xml_string = page.read()
    return xmltodict.parse(xml_string)


def eind_bestemming():
    eb = input('Wat is uw eindbestemming?')
    for i in stations()['ActueleVertrekTijden']['VertrekkendeTrein']:
        if i['EindBestemming'] == eb:
            vertrekkende_trein = dict(i)['VertrekTijd']
            print('Vertrek tijd is: ' + vertrekkende_trein[14:])



