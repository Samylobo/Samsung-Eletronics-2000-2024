import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import locale

# Definir a localização para o formato de moeda desejado
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

df = pd.read_csv('samsung.csv')
# Organização dos dados 
df['data'] = pd.to_datetime(df['data'], origin='1899-12-30', unit='D')
df['abertura'] = df['abertura'].astype(float)
df['alta'] = df['alta'].astype(float)
df['baixa'] = df['baixa'].astype(float)
df['fechamento'] = df['fechamento'].astype(float)
df['ajuste_proximo'] = df['ajuste_proximo'].astype(float)
df['volume'] = df['Volume'].astype(float) 
print(df.head())

# Menor 
menor_preco = df['baixa'].min()
print(f"O menor preço atingido pela ação durante o pregão foi: {locale.currency(menor_preco, grouping=True)}")

# Maior 
# Encontrar o maior preço (máximo) durante o pregão
maior_preco = df['alta'].max()
print(f"O maior preço atingido pela ação durante o pregão foi: {locale.currency(maior_preco, grouping=True)}")
 
# Calcular o valor médio das ações
valor_medio = df['ajuste_proximo'].mean()

# Imprimir o valor médio das ações
print(f"O valor médio das ações da Samsung foi de: {locale.currency(valor_medio, grouping=True)}")

#Plotar um gráfico de linha dos preços de fechamento ao longo do tempo
plt.figure(figsize=(12, 6))
sns.lineplot(x='data', y='fechamento', data=df)  # Corrigimos 'Date' para 'data' e 'Close' para 'fechamento'
plt.title('Preços de fechamento das ações da Samsung Electronics')
plt.xlabel('Data')
plt.ylabel('Preço de fechamento')
plt.show()

#corelação entre volume e preço de fechamento
plt.figure(figsize=(12, 6))
sns.lineplot(x='data', y='fechamento', data=df)  # Corrigimos 'Date' para 'data' e 'Close' para 'fechamento'
plt.xlabel('Correlacão entre Volume de Negociação e preco de fechamento')
plt.xlabel('Volume')
plt.xlabel('Preço de fechamento')
correlation = df['Volume'].corr(df['fechamento'])

print(f"Coeficiente de correlação entre Volume e Preço de Fechamento: {correlation}")










