# %% 

import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()

 # %%
import numpy as np

def diff_amp(x: pd.Series):
     amplitude = x.max() - x.min()
     media =  x.mean()
     return np.sqrt((amplitude - media)) ** 2

def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days

idades = pd.Series([21,32,43,32,14,65,78,34,19])

# %%

summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
           .agg({
               "IdTransacao": ['count'],
               "QtdePontos": ["sum", "mean", diff_amp],
               "DtCriacao": [life_time]
           }) 
)

summary.columns = [
    "idCliente",
    "qtdeTransacao",
    "totalPontos",
    "mediaPontos",
    "ampMeanDiff",
    "lifeTime",
]

summary