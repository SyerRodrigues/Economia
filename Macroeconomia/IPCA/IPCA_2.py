import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df_m2 = pd.read_excel('dados_m2.xlsx', sheet_name='base')
df_ipca = pd.read_excel('dados_IPCA.xlsx', sheet_name='base')

# Garantir que os nomes das colunas sejam consistentes
df_m2.rename(columns={'Data M2': 'Data'}, inplace=True)
df_ipca.rename(columns={'Data Ipca': 'Data'}, inplace=True)

# Limpar as colunas de data (remover espaços e ajustar formato, se necessário)
df_m2['Data'] = df_m2['Data'].astype(str).str.strip().str.replace(',', '.', regex=False)
df_ipca['Data'] = df_ipca['Data'].astype(str).str.strip().str.replace(',', '.', regex=False)

# Converter as colunas de data para o formato datetime
df_m2['Data'] = pd.to_datetime(df_m2['Data'], format='%Y.%m', errors='coerce')
df_ipca['Data'] = pd.to_datetime(df_ipca['Data'], format='%Y.%m', errors='coerce')

# Limpar dados: remover linhas onde a Data está nula
df_m2.dropna(subset=['Data'], inplace=True)
df_ipca.dropna(subset=['Data'], inplace=True)

# Calcular a variação percentual do M2
df_m2['Variacao_Percentual_M2'] = df_m2['M2'].pct_change() * 100

# Calcular a variação percentual do IPCA
df_ipca['Variacao_Percentual_IPCA'] = df_ipca['IPCA'].pct_change() * 100

# Plotar o gráfico de M2 para todo o período
plt.figure(figsize=(10, 5))
plt.plot(df_m2['Data'], df_m2['M2'], label='M2', color='orange')
plt.title('M2 - Todo o Período')
plt.xlabel('Data')
plt.ylabel('M2')
plt.legend()
plt.show()

# Filtrar os dados para o período de agosto de 1988 a junho de 1994
df_m2_periodo = df_m2[(df_m2['Data'] >= '1988-08-01') & (df_m2['Data'] <= '1994-06-30')]
df_ipca_periodo = df_ipca[(df_ipca['Data'] >= '1988-08-01') & (df_ipca['Data'] <= '1994-06-30')]

# Verificar se os DataFrames filtrados não estão vazios
if not df_m2_periodo.empty and not df_ipca_periodo.empty:
    # Plotar o gráfico da taxa de variação de M2 e IPCA
    plt.figure(figsize=(10, 5))
    plt.plot(df_m2_periodo['Data'], df_m2_periodo['Variacao_Percentual_M2'], label='Variação % M2', color='orange')
    plt.plot(df_ipca_periodo['Data'], df_ipca_periodo['Variacao_Percentual_IPCA'], label='Variação % IPCA', color='blue')
    plt.title('Taxa de Variação de M2 e IPCA (1988.08 - 1994.06)')
    plt.xlabel('Data')
    plt.ylabel('Variação Percentual')
    plt.legend()
    plt.show()
else:
    print("Um ou ambos os DataFrames filtrados estão vazios. Verifique os dados de entrada.")