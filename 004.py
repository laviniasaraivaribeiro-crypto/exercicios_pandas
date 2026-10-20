#Imprima todos os  detalhes dos carros da Toyota

import pandas as pd

# 1. Carregar os dados limpos
df_clean = pd.read_csv("dados_limpos.csv")

# 2. Filtrar e imprimir apenas os carros da Toyota
toyota_df = df_clean[df_clean["company"] == "toyota"]
print(toyota_df)