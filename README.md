#  Análise de Dados de Empresas Unicórnios 

## Empresas Unicórnios: 
Empresas unicórnios são startups que atingiram uma avaliação de mercado de pelo menos 1 bilhão de dólares antes de se tornarem públicas ou serem adquiridas. O termo foi popularizado por Aileen Lee, uma capitalista de risco, em 2013, e simboliza a raridade dessas empresas, assim como a mitológica criatura do unicórnio.

Nesse Projeto foi desenvolvido aplicações do pandas para facilitar a análise de dados graficamente da tabela de startups que tiveram seu desenvolvimento no ano 2021, assim pode-se comparar os valores e paises participantes.

As principais habilidades desenvolvidas são referidas aos códigos de plotagem por meio de matplotlib e seabox com o auxílio do pandas, o código abaixo referencia partes significativas do código teste_data_analysis.py:

``` python



#Aplicação Matplotlib:

#Plotagem em forma de Gráfico de Barras
plt.bar(data_frame['Setor'].value_counts().index,data_frame['Setor'].value_counts())

#Plotagem em forma de Gráfico de Pizza
plt.pie((data_frame['País'].value_counts(normalize=True)*100).head(5),labels=data_frame['País'].value_counts().index[0:5],shadow=True,startangle=90,autopct='%1.1f%%' )

# Plotagem em forma de Gráfico de Linha
plt.plot(Analise_preco['País'],Analise_preco['Valor'])


# Aplicação do pandas

# Lendo o arquivo através de pandas
data_frame = pd.read_csv('Startups+in+2021+end.csv')

# como obter em forma de porcentagem
data_frame['Setor'].value_counts(normalize = True)

# Criando colunas e organizando as datas
data_frame['Mês']= pd.DatetimeIndex(data_frame['Data de Adesão']).month
data_frame['Ano']= pd.DatetimeIndex(data_frame['Data de Adesão']).year
data_frame['Dia'] = pd.DatetimeIndex(data_frame['Data de Adesão']).day


# A partir do groubpy, agrupando a tabela
Analise_Agrupada = data_frame.groupby( by=['País','Ano','Mês','Empresa']).count()['Id'].reset_index()

# o uso de loc para alterar informações de tabela
Analise_Agrupada.loc[Analise_Agrupada['País']=='Brazil']

```
