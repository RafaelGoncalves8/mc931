#!/usr/bin/python

__author__ = 'rodolfo'

import csv
import sys
import time
import geopy

def ConverteCidades(cidades):
    g = geopy.geocoders.GoogleV3()
    geoLista = []
    for cidade in cidades:
        print(cidade[0])
        time.sleep(2)
        if (len(cidade) == 1):
            try:
                endereco, (lat, long) = g.geocode(cidade[0])
                geoLista.append([cidade[0], lat, long])
            except geopy.exc.GeocoderTimedOut:
                geoLista.append(cidade)
        else:
            geoLista.append(cidade)
    return geoLista

if (len(sys.argv) != 2):
    print('Uso: %s cidades.csv' % sys.argv[0])
    sys.exit(1)
else:
    cidades = csv.reader(open(sys.argv[1]))
    geoLista = ConverteCidades(cidades)
    csv.writer(open('geo' + sys.argv[1], 'wt')).writerows(geoLista)
