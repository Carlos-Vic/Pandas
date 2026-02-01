# %%

import pandas as pd

df = pd.read_csv("../dia02/ufs.csv", sep=";")
df.head()

# %%

def str_to_float(x):
    x = float(x.replace(" ", "")
              .replace(",", ".")
              .replace("\xa0", ""))
    return x

# %%

df["Área (km²)"] = df["Área (km²)"].apply(str_to_float)
df["População (Censo 2022)"] = df["População (Censo 2022)"].apply(str_to_float)
df["PIB (2015)"] = df["PIB (2015)"].apply(str_to_float)
df["PIB per capita (R$) (2015)"] = df["PIB per capita (R$) (2015)"].apply(str_to_float)

# %%

def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"

df["Região"] = df["Unidade federativa"].apply(uf_to_regiao)
df

# %%

def mortalidade_to_float(x):
    x = float(x.replace("‰", "")
              .replace(",", "."))
    return x

df["Mortalidade infantil (2016)"] = df["Mortalidade infantil (2016)"].apply(mortalidade_to_float)

# %%

 # Se PIB / Capita > 30.000 +
# Mortalidade < 15 / 10000 + 
# IDH > 700

def classifica_bom(linha):
    return ((linha["PIB per capita (R$) (2015)"] > 30000) and 
            (linha["Mortalidade infantil (2016)"] < 15) and 
            (linha["IDH (2010)"] > 700))

df.apply(classifica_bom, axis=1)