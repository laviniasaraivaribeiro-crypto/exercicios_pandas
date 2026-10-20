#Encontre o nome de montadora de carros mais cara
import pandas as pd

# 1. Carregar os dados limpos gerados no exercício anterior
df_clean = pd.read_csv("dados_limpos.csv")

# 2. Código para encontrar o carro mais caro individualmente
mais_caro_carro = df_clean[df_clean["price"] == df_clean["price"].max()]
print(mais_caro_carro[["company", "price"]])

# 3. Código para encontrar a montadora com a maior média de preço
media_montadoras = df_clean.groupby("company")["price"].mean().sort_values(ascending=False)
print(media_montadoras.head(1))
