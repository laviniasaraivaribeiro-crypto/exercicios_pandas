#Combine dois data frames usando a seguinte condição:
#Crie dois data frame usando os dois dicionários a seguir, mescle os dois data frames e anexe o segundo data frame como uma nova coluna do primeiro data frame.

import pandas as pd

# Dicionários fornecidos
Car_price = {'Company': ['Toyota', 'Honda', 'Bmv', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
Car_horsepower = {'Company': ['Toyota', 'Honda', 'Bmv', 'Audi'], 'horsepower': [141, 80, 182, 160]}

# Criar os dois DataFrames
df_price = pd.DataFrame(Car_price)
df_horsepower = pd.DataFrame(Car_horsepower)

# Anexar a coluna 'horsepower' do segundo DataFrame ao primeiro
df_combinado = df_price.copy()
df_combinado['horsepower'] = df_horsepower['horsepower']

print("DataFrame combinado (coluna anexada):")
print(df_combinado)

import pandas as pd

# Dicionários fornecidos
Car_price = {'Company': ['Toyota', 'Honda', 'Bmv', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
Car_horsepower = {'Company': ['Toyota', 'Honda', 'Bmv', 'Audi'], 'horsepower': [141, 80, 182, 160]}

# Criar os dois DataFrames
df_price = pd.DataFrame(Car_price)
df_horsepower = pd.DataFrame(Car_horsepower)

# Mesclar os DataFrames pela coluna 'Company'
df_mesclado = pd.merge(df_price, df_horsepower, on='Company')

print("DataFrame mesclado por Company:")
print(df_mesclado)