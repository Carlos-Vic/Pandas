# %%
import requests
import pandas as pd

url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
resp.raise_for_status()

dfs = pd.read_html(resp.text)
dfs

# %%
df = dfs[1]
df
df.to_csv('ufs.csv', index=False, sep=';')