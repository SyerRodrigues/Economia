import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.filters.hp_filter import hpfilter

# Dados da taxa de desocupação do Brasil
trimestres = [
    '1º trimestre 2012', '2º trimestre 2012', '3º trimestre 2012', '4º trimestre 2012',
    '1º trimestre 2013', '2º trimestre 2013', '3º trimestre 2013', '4º trimestre 2013',
    '1º trimestre 2014', '2º trimestre 2014', '3º trimestre 2014', '4º trimestre 2014',
    '1º trimestre 2015', '2º trimestre 2015', '3º trimestre 2015', '4º trimestre 2015',
    '1º trimestre 2016', '2º trimestre 2016', '3º trimestre 2016', '4º trimestre 2016',
    '1º trimestre 2017', '2º trimestre 2017', '3º trimestre 2017', '4º trimestre 2017',
    '1º trimestre 2018', '2º trimestre 2018', '3º trimestre 2018', '4º trimestre 2018',
    '1º trimestre 2019', '2º trimestre 2019', '3º trimestre 2019', '4º trimestre 2019',
    '1º trimestre 2020', '2º trimestre 2020', '3º trimestre 2020', '4º trimestre 2020',
    '1º trimestre 2021', '2º trimestre 2021', '3º trimestre 2021', '4º trimestre 2021',
    '1º trimestre 2022', '2º trimestre 2022', '3º trimestre 2022', '4º trimestre 2022',
    '1º trimestre 2023', '2º trimestre 2023', '3º trimestre 2023', '4º trimestre 2023',
    '1º trimestre 2024', '2º trimestre 2024', '3º trimestre 2024'
]
taxa_desocupacao = [
    8, 7.6, 7.1, 6.9, 8.1, 7.5, 7, 6.3, 7.2, 6.9, 6.9, 6.6, 
    8, 8.4, 9, 9.1, 11.1, 11.4, 11.9, 12.2, 13.9, 13.1, 12.5, 
    11.9, 13.2, 12.6, 12, 11.7, 12.8, 12.1, 11.9, 11.1, 12.4, 
    13.6, 14.9, 14.2, 14.9, 14.2, 12.6, 11.1, 11.1, 9.3, 8.7, 
    7.9, 8.8, 8, 7.7, 7.4, 7.9, 6.9, 6.4
]

# Verificação do tamanho das listas
if len(trimestres) != len(taxa_desocupacao):
    raise ValueError("As listas de trimestres e taxas de desocupação devem ter o mesmo comprimento.")

# Criar DataFrame para a taxa de desocupação do Brasil
df_brasil = pd.DataFrame({'Trimestre': trimestres, 'Taxa Desocupacao': taxa_desocupacao})

# Ajustar o formato das strings de data
def converter_trimestre_para_data(trimestre):
    partes = trimestre.split(' ')
    trimestre_num = int(partes[0][0])  # Primeiro caractere do primeiro elemento
    ano = partes[-1]  # Último elemento é o ano
    mes = (trimestre_num - 1) * 3 + 1  # Calcula o mês correspondente ao trimestre
    return f"{ano}-{mes:02d}-01"  # Retorna no formato YYYY-MM-DD

# Aplicar a conversão
df_brasil['Trimestre'] = [converter_trimestre_para_data(t) for t in df_brasil['Trimestre']]

# Converter para datetime
df_brasil['Trimestre'] = pd.to_datetime(df_brasil['Trimestre'])

# Aplicar o filtro HP na série do Brasil
df_brasil['Tendencia'], df_brasil['Ciclo'] = hpfilter(df_brasil['Taxa Desocupacao'], lamb=1600)

# Dados da taxa de desemprego dos EUA
data_us = {
    'observation_date': [
        '1º trimestre 2012', '2º trimestre 2012', '3º trimestre 2012', '4º trimestre 2012',
        '1º trimestre 2013', '2º trimestre 2013', '3º trimestre 2013', '4º trimestre 2013',
        '1º trimestre 2014', '2º trimestre 2014', '3º trimestre 2014', '4º trimestre 2014',
        '1º trimestre 2015', '2º trimestre 2015', '3º trimestre 2015', '4º trimestre 2015',
        '1º trimestre 2016', '2º trimestre 2016', '3º trimestre 2016', '4º trimestre 2016',
        '1º trimestre 2017', '2º trimestre 2017', '3º trimestre 2017', '4º trimestre 2017',
        '1º trimestre 2018', '2º trimestre 2018', '3º trimestre 2018', '4º trimestre 2018',
        '1º trimestre 2019', '2º trimestre 2019', '3º trimestre 2019', '4º trimestre 2019',
        '1º trimestre 2020', '2º trimestre 2020', '3º trimestre 2020', '4º trimestre 2020',
        '1º trimestre 2021', '2º trimestre 2021', '3º trimestre 2021', '4º trimestre 2021',
        '1º trimestre 2022', '2º trimestre 2022', '3º trimestre 2022', '4º trimestre 2022',
        '1º trimestre 2023', '2º trimestre 2023', '3º trimestre 2023', '4º trimestre 2023',
        '1º trimestre 2024', '2º trimestre 2024', '3º trimestre 2024'
    ],
    'UNRATE': [
        8.3, 8.2, 8.0, 7.8, 7.7, 7.5, 7.2, 6.9, 6.7, 6.2, 6.1, 5.7, 5.5, 5.4, 5.1, 
        5.0, 4.9, 4.9, 4.9, 4.8, 4.6, 4.4, 4.3, 4.2, 4.0, 3.9, 3.8, 3.8, 3.9, 3.6, 
        3.6, 3.6, 3.8, 13.0, 8.8, 6.7, 6.2, 5.9, 5.1, 4.2, 3.8, 3.6, 3.5, 3.6, 3.5, 
        3.6, 3.7, 3.7, 3.8, 4.0, 4.2
    ]
}

# Verificação do tamanho das listas de dados dos EUA
print("Número de datas:", len(data_us['observation_date']))
print("Número de taxas de desemprego:", len(data_us['UNRATE']))

# Criar DataFrame para os dados dos EUA
df_us = pd.DataFrame(data_us)

# Ajustar o formato das strings de data
df_us['observation_date'] = [converter_trimestre_para_data(t) for t in df_us['observation_date']]

# Converter para datetime
df_us['observation_date'] = pd.to_datetime(df_us['observation_date'])

# Verificar se há dados ausentes
df_us['UNRATE'] = pd.to_numeric(df_us['UNRATE'], errors='coerce')  # Corrigir a formatação
missing_data = df_us[df_us['UNRATE'].isna()]
print("Dados ausentes:")
print(missing_data)

# Verifique se os dados estão completos
if len(data_us['observation_date']) != len(data_us['UNRATE']):
    raise ValueError("As listas de observation_date e UNRATE devem ter o mesmo comprimento.")

# Transformar os dados mensais em trimestrais
df_us.set_index('observation_date', inplace=True)
df_us_quarterly = df_us.resample('Q').mean()

# Aplicar o filtro HP na série dos EUA
df_us_quarterly['Tendencia'], df_us_quarterly['Ciclo'] = hpfilter(df_us_quarterly['UNRATE'], lamb=1600)

# Plotar a série de desocupação do Brasil
plt.figure(figsize=(12, 6))
plt.plot(df_brasil['Trimestre'], df_brasil['Taxa Desocupacao'], label='Taxa de Desocupação Brasil', marker='o')
plt.plot(df_brasil['Trimestre'], df_brasil['Tendencia'], label='Tendência (Filtro HP)', linestyle='--')
plt.title('Taxa de Desocupação do Brasil e Tendência (Filtro HP)')
plt.xlabel('Trimestre')
plt.ylabel('Taxa de Desocupação (%)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Plotar a série de desemprego dos EUA
plt.figure(figsize=(12, 6))
plt.plot(df_us_quarterly.index, df_us_quarterly['UNRATE'], label='Taxa de Desemprego EUA', marker='o')
plt.plot(df_us_quarterly.index, df_us_quarterly['Tendencia'], label='Tendência (Filtro HP)', linestyle='--')
plt.title('Taxa de Desemprego nos EUA e Tendência (Filtro HP)')
plt.xlabel('Data')
plt.ylabel('Taxa de Desemprego (%)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Comparação das taxas de desocupação do Brasil e desemprego dos EUA
plt.figure(figsize=(12, 6))
plt.plot(df_brasil['Trimestre'], df_brasil['Tendencia'], label='Tendência Desocupação Brasil', marker='o')
plt.plot(df_us_quarterly.index, df_us_quarterly['Tendencia'], label='Tendência Desemprego EUA', linestyle='--')
plt.title('Comparação das Taxas de Desemprego: Brasil e EUA')
plt.xlabel('Data')
plt.ylabel('Taxa (%)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Análise dos períodos em que a taxa de desocupação do Brasil ficou acima de uma taxa natural
taxa_natural_brasil = 10  # Exemplo de taxa natural de desemprego para o Brasil
periodos_acima_taxa_natural = df_brasil[df_brasil['Taxa Desocupacao'] > taxa_natural_brasil]
print("Períodos em que a taxa de desocupação do Brasil ficou acima da taxa natural:")
print(periodos_acima_taxa_natural) 