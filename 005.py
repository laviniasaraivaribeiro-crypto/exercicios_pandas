#Conte  o total  de carros  por empresa
import pandas as pd

# Carregar os dados limpos
df_clean = pd.read_csv("dados_limpos.csv")

# Contar o total de carros por empresa
total_por_empresa = df_clean["company"].value_counts()

print("Total de carros por empresa:")
print(total_por_empresa)