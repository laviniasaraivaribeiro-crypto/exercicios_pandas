#Encontre o carro com o preço mais alto de cada empresa
import pandas as pd

# Carregar os dados limpos
df_clean = pd.read_csv("dados_limpos.csv")

# Agrupar por empresa e obter o maior preço de cada uma
preco_max_por_empresa = df_clean.groupby("company")["price"].max().reset_index()

print("Carro com o preço mais alto de cada empresa:")
print(preco_max_por_empresa)