#Calcule a quilometragem media de cada fabricante de auto-moveis
import pandas as pd

# Carregar os dados limpos
df_clean = pd.read_csv("dados_limpos.csv")

# Calcule a quilometragem média (average-mileage) por fabricante
media_km_por_empresa = df_clean.groupby("company")["average-mileage"].mean().reset_index()

print("Quilometragem média por fabricante:")
print(media_km_por_empresa)