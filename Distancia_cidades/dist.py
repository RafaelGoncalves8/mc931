import pandas as pd

cidades = pd.read_csv("cidades.csv")

for i, name, lat, lon, dist in enumerate(cidades):
    dist = 6371*
