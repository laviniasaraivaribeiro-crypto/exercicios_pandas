#Contatena dois data usando os dois dicionários a seguir:
import pandas as pd

# Dicionário com os dados dos carros alemães
german_cars_dict = {
    'Company': ['FORD', 'MERCEDES', 'BMW', 'AUDI'],
    'PRICE': [23845, 135925, 171995, 71400]
}

# Criar o DataFrame
GermanCars = pd.DataFrame(german_cars_dict)

print("DataFrame GermanCars:")
print(GermanCars)