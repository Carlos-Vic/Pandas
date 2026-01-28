#%%
# 04.01 - Quantos clientes tem vínculo com a Twitch?

import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv", sep=";")

filtro = clientes["flTwitch"] == 1
clientes_twitch = clientes[filtro]
clientes_twitch.shape[0]

#%%
# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?

filtro = clientes["qtdePontos"] > 1000
clientes_pontos = clientes[filtro]
clientes_pontos.shape[0]

#%%
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

filtro = (transacoes["DtCriacao"] >= '2025-02-01') & (transacoes["DtCriacao"] < '2025-02-02')
transacoes_fev = transacoes[filtro]
transacoes_fev.shape[0]