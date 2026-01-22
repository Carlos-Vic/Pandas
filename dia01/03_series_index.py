# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

series_idades = pd.Series(idades)
series_idades
# %%
idades[-1]
# %%

# .iloc[] acessa pela posição,"ignorando a chave"
series_idades.iloc[-1]

# %%

indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato"
]

series_idades = pd.Series(idades, index = indexs)
series_idades
# %%
series_idades.iloc[-1]
# series_idades[-1] Gera um KeyError
series_idades["Kozato"]