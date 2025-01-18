import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df_m2 = pd.read_excel('dados_m2.xlsx', sheet_name='base')
df_ipca = pd.read_excel('dados_IPCA.xlsx', sheet_name='base')

# Imprimir os nomes das colunas e os primeiros registros de cada DataFrame
print("Dados M2:")
print(df_m2.columns)
print(df_m2.head())
print("\nDados IPCA:")
print(df_ipca.columns)
print(df_ipca.head())

# Garantir que os nomes das colunas sejam consistentes
df_m2.rename(columns={'Data M2': 'Data'}, inplace=True)
df_ipca.rename(columns={'Data Ipca': 'Data'}, inplace=True)

# Limpar as colunas de data (remover espaços e ajustar formato, se necessário)
df_m2['Data'] = df_m2['Data'].astype(str).str.strip().str.replace(',', '.', regex=False)
df_ipca['Data'] = df_ipca['Data'].astype(str).str.strip().str.replace(',', '.', regex=False)

# Converter as colunas de data para o formato datetime
df_m2['Data'] = pd.to_datetime(df_m2['Data'], format='%Y.%m', errors='coerce')
df_ipca['Data'] = pd.to_datetime(df_ipca['Data'], format='%Y.%m', errors='coerce')

# Verificar se a conversão foi bem-sucedida
print("Tipos de dados após conversão:")
print(df_m2.dtypes)
print(df_ipca.dtypes)

# Verificar valores únicos após conversão
print("Datas únicas em M2:")
print(df_m2['Data'].unique())
print("Datas únicas em IPCA:")
print(df_ipca['Data'].unique())

# Limpar dados: remover linhas onde a Data está nula
df_m2.dropna(subset=['Data'], inplace=True)
df_ipca.dropna(subset=['Data'], inplace=True)

# Verificar interseção de datas
print("Datas comuns entre M2 e IPCA:")
datas_comuns = set(df_m2['Data']).intersection(set(df_ipca['Data']))
print(datas_comuns)

# Unir os DataFrames com base na data
df = pd.merge(df_m2, df_ipca, on='Data', how='inner')

# Verificar o DataFrame resultante
print("DataFrame após mesclagem:")
print(df.head())
print("Total de linhas após mesclagem:", len(df))

# Ordenar o DataFrame por data antes de calcular a variação percentual
df.sort_values(by='Data', inplace=True)

# Calcular a variação percentual do M2
df['Variacao_Percentual_M2'] = df['M2'].pct_change() * 100

# Calcular a variação percentual do IPCA
df['Variacao_Percentual_IPCA'] = df['IPCA'].pct_change() * 100

# Verificar se há valores nulos
print("Valores nulos no DataFrame mesclado:")
print(df.isnull().sum())

# Plotar os gráficos apenas se o DataFrame não estiver vazio
if not df.empty:
    # Gráfico 1: IPCA - Todo o Período
    plt.figure(figsize=(10, 5))
    plt.plot(df['Data'], df['IPCA'])
    plt.title('IPCA - Todo o Período')
    plt.xlabel('Data')
    plt.ylabel('IPCA')
    plt.show()

    # Gráfico 2: IPCA 1980-1994.06
    plt.figure(figsize=(10, 5))
    plt.plot(df['Data'], df['IPCA'])
    plt.xlim(pd.Timestamp('1980-01-01'), pd.Timestamp('1994-06-30'))
    plt.title('IPCA - 1980 a 1994.06')
    plt.xlabel('Data')
    plt.ylabel('IPCA')
    plt.show()

    # Gráfico 3: IPCA 1994.07 em diante
    plt.figure(figsize=(10, 5))
    plt.plot(df['Data'], df['IPCA'])
    plt.xlim(pd.Timestamp('1994-07-01'), df['Data'].max())
    plt.title('IPCA - 1994.07 em diante')
    plt.xlabel('Data')
    plt.ylabel('IPCA')
    plt.show()

    # Gráfico 4: Variação Percentual de M2 e IPCA 1988.08-1994.06
    plt.figure(figsize=(10, 5))
    plt.plot(df['Data'], df['Variacao_Percentual_M2'], label='Variação % M2', color='orange')
    plt.plot(df['Data'], df['Variacao_Percentual_IPCA'], label='Variação % IPCA', color='blue')
    plt.xlim(pd.Timestamp('1988-08-01'), pd.Timestamp('1994-06-30'))
    plt.title('Variação % M2 e IPCA - 1988.08 a 1994.06')
    plt.xlabel('Data')
    plt.ylabel('Variação Percentual')
    plt.legend()
    plt.show()
else:
    print("O DataFrame está vazio. Verifique os dados de entrada.")