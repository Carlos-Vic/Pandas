# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

nomes = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame()
df["Idades"] = series_idades
df["Nomes"] = series_nomes
#%%

df.iloc[0] # Retorna uma linha como série com os indices sendo as colunas
df.iloc[0]["Nomes"] # Retorna o valor da coluna "Nomes" da primeira linha

# %%

df.iloc[-1]["Idades"] # Retorna a ultima idade do dataframe