import pandas as pd


def filter_by_year(ano):
    return df[df['ano'] == ano]


def filter_by_year_and_uf(ano, uf):
    fy = filter_by_year(ano)
    return fy[fy['UF'] == uf]['numero']


data = pd.read_csv('graduacao_br.csv', delimiter=",")
df = pd.read_csv('complete.csv', delimiter=",")


cidades_set = set(df.cidade)
# print(sum(df[ (df["cidade"] == "Campinas") and (df['ano'] == 2017) ]["numero"]))

D = {str(i): None for i in range(1997,2018)}

for ano in range(1997, 2018):
    D[str(ano)] = (1 - sum(filter_by_year_and_uf(ano, 'SP'))/sum(filter_by_year(ano)['numero']))

#print(sum(filter_by_city_and_number.numero))
print(D)


