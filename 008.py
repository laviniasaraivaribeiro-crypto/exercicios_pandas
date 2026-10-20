#Ordene todos os carros pela coluna de preços
import pandas as pd

# Carregar os dados limpos
df_clean = pd.read_csv("dados_limpos.csv")

# Ordenar carros do menor para o maior preço
carros_ordenados_crescente = df_clean.sort_values(by="price", ascending=True)

print("Carros ordenados pelo preço (mais baratos primeiro):")
print(carros_ordenados_crescente[["company", "body-style", "price"]])

import pandas as pd

# Carregar os dados limpos
df_clean = pd.read_csv("dados_limpos.csv")

# Ordenar carros do maior para o menor preço
carros_ordenados_decrescente = df_clean.sort_values(by="price", ascending=False)

print("Carros ordenados pelo preço (mais caros primeiro):")
print(carros_ordenados_decrescente[["company", "body-style", "price"]])