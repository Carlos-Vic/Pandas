#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

#%%
df.shape

# %%
df.info(memory_usage="deep")

#%%
df.dtypes

#%%
renamed_columns = {
    "QtdePontos": "qtPontos",
    "DescSistemaOrigem": "SistemaOrigem"
}

#df = df.rename(columns=renamed_columns)
df.rename(columns=renamed_columns, inplace=True)

#%%

df[["IdCliente"]]
# %%

# SELECT * FROM df
df
#%%

# SELECT IdCliente FROM df
df[["IdCliente"]]

# %%

# SELECT IdCliente, qtPontos FROM df LIMIT 5

df[["IdCliente", "qtPontos"]].tail(5)

# %%

colunas = df.columns.tolist()
colunas.sort()
colunas

df = df[colunas]
df