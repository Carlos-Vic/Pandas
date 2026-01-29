# %%

import pandas as pd
import numpy as np

# %%

# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch

df = pd.read_csv("../../data/clientes.csv", sep=";")
df["twitch_points"] = df["flTwitch"] * df["qtdePontos"]
df

# %%

# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova

df["log_Pontos"] = np.log(df["qtdePontos"] + 1)
df

# %%

# 05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.

df["tem_social"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df

# %%

# 05.04 -  Qual é o id de cliente que tem maior saldo de pontos? E o menor?

maior_saldo = df.sort_values("qtdePontos", ascending=False)["idCliente"].iloc[0]
menor_saldo = df.sort_values("qtdePontos", ascending=False)["idCliente"].iloc[-1]
print(f"Maior saldo de pontos: {maior_saldo}")
print(f"Menor saldo de pontos: {menor_saldo}")

# %%

# 05.05 - Selecione a primeira transação diária de cada cliente.

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

transacoes = transacoes.sort_values("DtCriacao")
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes = transacoes.drop_duplicates(keep='first', subset=['IdCliente', 'data'])
transacoes