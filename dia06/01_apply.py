# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%

def get_last_id(x):
    return x.split("-")[-1]

id_novo = []
for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo
df.head()

# %%

df["idCliente"].apply(get_last_id)
