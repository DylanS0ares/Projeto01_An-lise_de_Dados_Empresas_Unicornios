
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



data_frame = pd.read_csv('Startups+in+2021+end.csv')

# renomeando as colunas

data_frame.rename( columns = {
'Unnamed: 0':'Id',
 'Company':'Empresa',
 'Valuation ($B)':'Valor',
 'Date Joined':'Data de Adesão',
 'Country':'País',
 'City':'Cidade',
 'Industry': 'Setor',
 'Select Investors':'Investidores',
      
}, inplace = True)



# Gráfico de calor

plt.figure(figsize=(10,6))
sns.heatmap(data_frame.isnull(),cbar=False)
plt.title('Mapa de Calor de Valores Nulos')
plt.savefig('Mapa de Calor de Valores Nulos.png')
plt.show()



# Valores unicos na coluna setor
print(data_frame['País'].unique())

#Valores Unicos - Ran1 

#Normalize = True passa em forma de percentual 

print(data_frame['Setor'].value_counts(normalize = True))

plt.figure(figsize=(10,10))
plt.title("Analise dos Setores")
plt.ylabel('nº nos setores')
plt.xticks(rotation=45,ha = 'right')
plt.bar(data_frame['Setor'].value_counts().index,data_frame['Setor'].value_counts())
plt.subplots_adjust(bottom=0.2) 
plt.savefig('Gráfico Analise dos Setores.png')
plt.show()

# # Plot Geral dos Países top 5 em gráfico de pizza
plt.figure(figsize=(10,10))
plt.title('Países geradores de Unicórnios top 5')

plt.pie((data_frame['País'].value_counts(normalize=True)*100).head(5),labels=data_frame['País'].value_counts().index[0:5],shadow=True,startangle=90,autopct='%1.1f%%' )
plt.xticks(rotation=90,ha='right')
plt.savefig('Gráfico Países geradores de Unicórnios.png')
plt.show()

data_frame['País'].value_counts()

# Não foi selecionado o top 10 para não ficar poluido


data_frame['Data de Adesão'] = pd.to_datetime(data_frame['Data de Adesão'])



#print(data_frame['Data de Adesão'].dt.year)

data_frame['Mês']= pd.DatetimeIndex(data_frame['Data de Adesão']).month
data_frame['Ano']= pd.DatetimeIndex(data_frame['Data de Adesão']).year
data_frame['Dia'] = pd.DatetimeIndex(data_frame['Data de Adesão']).day
# tabela analitica
Analise_Agrupada = data_frame.groupby( by=['País','Ano','Mês','Empresa']).count()['Id'].reset_index()


# Analise da Tabela Analítica Brazil
Analise_Agrupada.loc[Analise_Agrupada['País']=='Brazil']

# Alterando a coluna Valor

data_frame['Valor']= pd.to_numeric(data_frame['Valor'].apply(lambda Linha: Linha.replace('$','')))

Analise_pais = data_frame.groupby(by=['País'])['Valor'].sum().reset_index()

Analise_preco= Analise_pais.sort_values('Valor',ascending=False)

plt.figure(figsize=(12,8))
plt.plot(Analise_preco['País'],Analise_preco['Valor'])
plt.title('Analise do Valor por País')
plt.xticks(rotation=45,ha='right')
plt.subplots_adjust(bottom=0.2)
plt.show()
plt.savefig('Gráfico Analise do Valor por País.png')
#

