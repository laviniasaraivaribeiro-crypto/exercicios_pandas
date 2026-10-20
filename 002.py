#Limpe o conjunto de dados e utilize o arquivo CSV

import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv("LAVINIA VITORIA SARAIVA RIBEIRO - Automobile_data - LAVINIA VITORIA SARAIVA RIBEIRO - Automobile_data.csv")

# 2. Limpar o dataset removendo linhas com valores nulos
df_clean = df.dropna()

# Para visualizar os dados limpos no terminal
print(df_clean)

# Para salvar os dados limpos num novo arquivo CSV
df_clean.to_csv("dados_limpos.csv", index=False)