# %%

import pandas as pd 

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.rename(columns={"idCliente": "IdCliente"}, inplace=True)
clientes.head()
# %%

transacoes.merge(right=clientes, 
                 how='left', 
                 on=['IdCliente'],
                 suffixes=(["Transacao", "Cliente"]))

# %%

