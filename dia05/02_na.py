# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%

clientes = clientes.dropna(how="all")

# %%

df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453, 4324, None, 5423]
    }
)

df.dropna(how="any", subset=["idade", "salario"])

# %%

df["idade"].fillna(0)

# %%

df.fillna({"nome": "alguem", "idade" : 0})

# %%

medias = df[["idade", "salario"]].mean()
df.fillna(medias)