# %%

# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?

import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv", sep=";")

clientes["redes_sociais"] = (clientes["flEmail"] + clientes["flTwitch"] + 
                             clientes["flYouTube"] + clientes["flBlueSky"] + 
                             clientes["flInstagram"])

media = clientes["redes_sociais"].mean()
variancia = clientes["redes_sociais"].var()
maximo = clientes["redes_sociais"].max()

print(f"Média: {media}")
print(f"Variância: {variancia}")
print(f"Máximo: {maximo}")

# %%

# 06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

(transacoes.groupby(by=["IdCliente"])["IdTransacao"]
                        .count()
                        .sort_values(ascending=False)
                        .head(10))

# %%

# 06.03 - Qual usuário teve maior quantidade de pontos debitados?

filtro = transacoes["QtdePontos"] < 0

(transacoes.groupby(by="IdCliente")["QtdePontos"]
                    .sum()
                    .sort_values(ascending=True)
                    .head(1))

# %%

# 06.04 - Quem teve mais transações de Streak?

transacao_produto = pd.read_csv("../../data/transacao_produto.csv", sep=";")
transacao_produto.head()

produtos = pd.read_csv("../../data/produtos.csv", sep=";")
produtos.head()

clientes_transacao_produto = transacoes.merge(
    transacao_produto, 
    on="IdTransacao", 
    how="left")[["IdTransacao", "IdCliente", "IdProduto"]]

df_full = clientes_transacao_produto.merge(
    produtos,
    on=["IdProduto"],
    how="left",
)

df_full = df_full[df_full["DescNomeProduto"] == "Presença Streak"]

(df_full.groupby(by="IdCliente")["IdTransacao"]
                                .count()
                                .sort_values(ascending=False)
                                .head(10)
)

# Maneira mais performática

produtos = produtos[produtos["DescNomeProduto"] == "Presença Streak"]

(transacoes.merge(transacao_produto, on="IdTransacao", how="left")
           .merge(produtos, on="IdProduto", how="left")
           .groupby(by="IdCliente")["IdTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(1)
)

# %%

