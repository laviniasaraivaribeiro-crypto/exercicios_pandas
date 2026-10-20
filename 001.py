#A partir  do conjunto de dados de dados fornecido, imprima as cinco primeiras e as cinco ultimas linhas.
import pandas as pd

import pandas as pd

# Carregar o DataFrame (supondo que o arquivo seja 'Automobile_data.csv')
df = pd.read_csv('LAVINIA VITORIA SARAIVA RIBEIRO - Automobile_data - LAVINIA VITORIA SARAIVA RIBEIRO - Automobile_data.csv')

# Exibir as 5 primeiras linhas
print("Primeiras 5 linhas:")
print(df.head(5))

# Exibir as 5 últimas linhas
print("\nÚltimas 5 linhas:")
print(df.tail(5))