import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



data_frame = pd.read_csv('Startups+in+2021+end.csv')


# Primeiros registros

#print(data_frame.head(5))



# verifica dimensões 
data_frame.shape

# colunas
print(data_frame.columns)

#renomear 

data_frame.rename( columns = {
'Unnamed: 0':'Id',
 'Company':'Empresa',
 'Valuation ($B)':'Valor',
 'Date Joined':'Data de Adesão',
 'Country':'País',
 'City':'Cidade',
 'Industry': 'Industria',
 'Select Investors':'Investidores',
      
}, inplace = True)

#tipo de cada coluna
data_frame.info()

# retorna o valor booleano
data_frame.isnull()

# Gráfico de calor

plt.figure(figsize=(10,6))
sns.heatmap(data_frame.isnull(),cbar=False)
plt.title('Mapa de Calor de Valores Nulos')
plt.show()