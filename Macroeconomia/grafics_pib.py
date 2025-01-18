import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.filters.hp_filter import hpfilter

# Criação do DataFrame com os dados do PIB
data_pib = {
    'Trimestre': ['1º trimestre 1996', '2º trimestre 1996', '3º trimestre 1996', '4º trimestre 1996',
                  '1º trimestre 1997', '2º trimestre 1997', '3º trimestre 1997', '4º trimestre 1997',
                  '1º trimestre 1998', '2º trimestre 1998', '3º trimestre 1998', '4º trimestre 1998',
                  '1º trimestre 1999', '2º trimestre 1999', '3º trimestre 1999', '4º trimestre 1999',
                  '1º trimestre 2000', '2º trimestre 2000', '3º trimestre 2000', '4º trimestre 2000',
                  '1º trimestre 2001', '2º trimestre 2001', '3º trimestre 2001', '4º trimestre 2001',
                  '1º trimestre 2002', '2º trimestre 2002', '3º trimestre 2002', '4º trimestre 2002',
                  '1º trimestre 2003', '2º trimestre 2003', '3º trimestre 2003', '4º trimestre 2003',
                  '1º trimestre 2004', '2º trimestre 2004', '3º trimestre 2004', '4º trimestre 2004',
                  '1º trimestre 2005', '2º trimestre 2005', '3º trimestre 2005', '4º trimestre 2005',
                  '1º trimestre 2006', '2º trimestre 2006', '3º trimestre 2006', '4º trimestre 2006',
                  '1º trimestre 2007', '2º trimestre 2007', '3º trimestre 2007', '4º trimestre 2007',
                  '1º trimestre 2008', '2º trimestre 2008', '3º trimestre 2008', '4º trimestre 2008',
                  '1º trimestre 2009', '2º trimestre 2009', '3º trimestre 2009', '4º trimestre 2009',
                  '1º trimestre 2010', '2º trimestre 2010', '3º trimestre 2010', '4º trimestre 2010',
                  '1º trimestre 2011', '2º trimestre 2011', '3º trimestre 2011', '4º trimestre 2011',
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
                  '1º trimestre 2024', '2º trimestre 2024', '3º trimestre 2024'],
    'PIB': [99.4, 100.66, 104.15, 103.38, 104.42, 105, 106.13, 107.22, 105.1, 106.81, 106.72, 105.65,
            105.82, 106.26, 106.36, 107.83, 109, 110.45, 111.97, 113.24, 113.5, 113.09, 112.6, 112.05,
            114.91, 115.31, 116.76, 117.9, 117.52, 116.54, 117.52, 118.74, 120.5, 123.75, 125.29,
            126.31, 127.38, 128.77, 128, 129.78, 131.6, 132.17, 134.38, 136.05, 138.39, 140.83,
            142.29, 144.36, 146.29, 149.27, 151.52, 145.86, 143.92, 146.46, 149.91, 153.67, 156.97,
            158.94, 160.34, 162.55, 164.92, 166.39, 166.11, 167.68, 165.33, 168.17, 171.1, 171.22,
            172.04, 174.52, 175.24, 175.58, 176.87, 174.56, 174.39, 175.15, 173.73, 169.79, 167.13,
            165.51, 163.25, 163.74, 162.91, 162.76, 164.32, 165.63, 166.18, 167.16, 167.93, 167.89,
            169.41, 169.06, 169.55, 170.55, 170.49, 171.89, 168.1, 153.26, 165.33, 171.45, 173.14,
            172.06, 172.26, 174.26, 175.75, 177.8, 179.56, 180.29, 182.77, 184.23, 184.6, 184.87,
            186.82, 189.41, 191.14]
}

# Criação do DataFrame do PIB
df_pib = pd.DataFrame(data_pib)

# Aplicando o logaritmo natural ao PIB
df_pib['log_PIB'] = np.log(df_pib['PIB'])

# Aplicando o filtro Hodrick-Prescott ao PIB
cycle_pib, trend_pib = hpfilter(df_pib['log_PIB'], lamb=1600)

# Adicionando as séries de tendência e cíclica ao DataFrame do PIB
df_pib['Trend'] = trend_pib
df_pib['Cycle'] = cycle_pib

# Criação de um DataFrame com os dados de Despesas de Consumo das Famílias
data_consumo = {
    'Trimestre': ['1º trimestre 1996', '2º trimestre 1996', '3º trimestre 1996', '4º trimestre 1996',
                  '1º trimestre 1997', '2º trimestre 1997', '3º trimestre 1997', '4º trimestre 1997',
                  '1º trimestre 1998', '2º trimestre 1998', '3º trimestre 1998', '4º trimestre 1998',
                  '1º trimestre 1999', '2º trimestre 1999', '3º trimestre 1999', '4º trimestre 1999',
                  '1º trimestre 2000', '2º trimestre 2000', '3º trimestre 2000', '4º trimestre 2000',
                  '1º trimestre 2001', '2º trimestre 2001', '3º trimestre 2001', '4º trimestre 2001',
                  '1º trimestre 2002', '2º trimestre 2002', '3º trimestre 2002', '4º trimestre 2002',
                  '1º trimestre 2003', '2º trimestre 2003', '3º trimestre 2003', '4º trimestre 2003',
                  '1º trimestre 2004', '2º trimestre 2004', '3º trimestre 2004', '4º trimestre 2004',
                  '1º trimestre 2005', '2º trimestre 2005', '3º trimestre 2005', '4º trimestre 2005',
                  '1º trimestre 2006', '2º trimestre 2006', '3º trimestre 2006', '4º trimestre 2006',
                  '1º trimestre 2007', '2º trimestre 2007', '3º trimestre 2007', '4º trimestre 2007',
                  '1º trimestre 2008', '2º trimestre 2008', '3º trimestre 2008', '4º trimestre 2008',
                  '1º trimestre 2009', '2º trimestre 2009', '3º trimestre 2009', '4º trimestre 2009',
                  '1º trimestre 2010', '2º trimestre 2010', '3º trimestre 2010', '4º trimestre 2010',
                  '1º trimestre 2011', '2º trimestre 2011', '3º trimestre 2011', '4º trimestre 2011',
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
                  '1º trimestre 2024', '2º trimestre 2024', '3º trimestre 2024'],
    'Despesas_Consumo': [98.63, 100.88, 103.93, 109.17, 106.42, 106.92, 106.09, 106.05, 105.9, 105.74,
                         106.16, 104.64, 104.9, 105.06, 106.1, 107.89, 108, 109.48, 111.25, 112.29,
                         112.27, 112.85, 109.32, 110.17, 112.47, 113.65, 112.37, 111.92, 112.4, 111.35,
                         111.61, 112.55, 113.38, 114.83, 117.1, 119.98, 119.4, 120.33, 122.21, 123.98,
                         125.33, 127.27, 128.59, 130.44, 133.33, 135.08, 135.93, 139.88, 142.9, 144.53,
                         147.23, 144.86, 146.12, 150.31, 153.79, 154.9, 157.01, 158.5, 161.96, 165.38,
                         166.94, 169.18, 168.51, 169.4, 171.77, 173.1, 175.35, 177.29, 178.16, 180.48,
                         181.61, 181.5, 184.46, 183.46, 183.66, 186.42, 183.23, 179.73, 176.42, 175.2,
                         172.92, 171.9, 171.29, 170.86, 171.98, 174.8, 176.52, 177.02, 178.39, 178.79,
                         179.82, 179.96, 182.58, 183.29, 184.35, 185.31, 183.46, 162.85, 174.73, 180.76,
                         180.94, 178.51, 181.24, 182.14, 184.22, 188.17, 189.69, 190.69, 191.72, 193.83,
                         195.79, 195.93, 200.79, 203.58, 206.57]
}

# Criação do DataFrame das Despesas de Consumo
df_consumo = pd.DataFrame(data_consumo)

# Aplicando o logaritmo natural às Despesas de Consumo
df_consumo['log_Despesas_Consumo'] = np.log(df_consumo['Despesas_Consumo'])

# Aplicando o filtro Hodrick-Prescott às Despesas de Consumo
cycle_consumo, trend_consumo = hpfilter(df_consumo['log_Despesas_Consumo'], lamb=1600)

# Adicionando as séries de tendência e cíclica ao DataFrame das Despesas de Consumo
df_consumo['Trend'] = trend_consumo
df_consumo['Cycle'] = cycle_consumo

# Criação de um DataFrame com os dados de Formação Bruta de Capital Fixo
data_investimento = {
    'Trimestre': ['1º trimestre 1996', '2º trimestre 1996', '3º trimestre 1996', '4º trimestre 1996',
                  '1º trimestre 1997', '2º trimestre 1997', '3º trimestre 1997', '4º trimestre 1997',
                  '1º trimestre 1998', '2º trimestre 1998', '3º trimestre 1998', '4º trimestre 1998',
                  '1º trimestre 1999', '2º trimestre 1999', '3º trimestre 1999', '4º trimestre 1999',
                  '1º trimestre 2000', '2º trimestre 2000', '3º trimestre 2000', '4º trimestre 2000',
                  '1º trimestre 2001', '2º trimestre 2001', '3º trimestre 2001', '4º trimestre 2001',
                  '1º trimestre 2002', '2º trimestre 2002', '3º trimestre 2002', '4º trimestre 2002',
                  '1º trimestre 2003', '2º trimestre 2003', '3º trimestre 2003', '4º trimestre 2003',
                  '1º trimestre 2004', '2º trimestre 2004', '3º trimestre 2004', '4º trimestre 2004',
                  '1º trimestre 2005', '2º trimestre 2005', '3º trimestre 2005', '4º trimestre 2005',
                  '1º trimestre 2006', '2º trimestre 2006', '3º trimestre 2006', '4º trimestre 2006',
                  '1º trimestre 2007', '2º trimestre 2007', '3º trimestre 2007', '4º trimestre 2007',
                  '1º trimestre 2008', '2º trimestre 2008', '3º trimestre 2008', '4º trimestre 2008',
                  '1º trimestre 2009', '2º trimestre 2009', '3º trimestre 2009', '4º trimestre 2009',
                  '1º trimestre 2010', '2º trimestre 2010', '3º trimestre 2010', '4º trimestre 2010',
                  '1º trimestre 2011', '2º trimestre 2011', '3º trimestre 2011', '4º trimestre 2011',
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
                  '1º trimestre 2024', '2º trimestre 2024', '3º trimestre 2024'],
    'Formacao_Capital': [96.84, 98.71, 102.41, 106.78, 107.69, 109.2, 111.34, 110.61, 111.21, 111.62,
                         110.18, 105.22, 101.47, 100.23, 97.89, 99.88, 100.6, 104.67, 104.7, 108.46,
                         110.35, 107.5, 105.98, 100.06, 101.3, 103.62, 105.24, 107.47, 104.37, 97.03,
                         97.68, 102.06, 105.47, 108.94, 111.14, 109.28, 107.31, 112.37, 111.68, 111.89,
                         117.36, 116.59, 117.58, 121.33, 126.4, 131.42, 133.76, 137.49, 142.14, 149.83,
                         157.34, 144.62, 128.98, 137.75, 151.1, 163, 166.53, 169.38, 174.4, 175.67,
                         179.78, 183, 185.13, 185.46, 184.55, 184.81, 183.19, 186.89, 189.05, 200.25,
                         197.43, 195.43, 196.11, 187.47, 183.09, 182.75, 177.18, 164.85, 155.61,
                         147.35, 144.01, 147.6, 138.65, 136.1, 136.6, 136.51, 137.03, 141.43, 141.27,
                         142.11, 149.58, 147.2, 145.42, 152.85, 157, 148.33, 155.58, 130.72, 143.37,
                         163.55, 173.74, 165.39, 164.99, 166.15, 163.47, 168.53, 173.55, 171.42, 166.01,
                         165.8, 161.53, 163.93, 171.35, 175.07, 178.69]
}
# Criação do DataFrame da Formação Bruta de Capital Fixo
df_investimento = pd.DataFrame(data_investimento)

# Aplicando o logaritmo natural à Formação Bruta de Capital
df_investimento['log_Formacao_Capital'] = np.log(df_investimento['Formacao_Capital'])

# Aplicando o filtro Hodrick-Prescott à Formação Bruta de Capital
cycle_investimento, trend_investimento = hpfilter(df_investimento['log_Formacao_Capital'], lamb=1600)

# Adicionando as séries de tendência e cíclica ao DataFrame da Formação Bruta de Capital
df_investimento['Trend'] = trend_investimento
df_investimento['Cycle'] = cycle_investimento

# Criação do DataFrame da Indústria
data_industria = {
    'Trimestre': ['1º trimestre 1996', '2º trimestre 1996', '3º trimestre 1996', '4º trimestre 1996',
                  '1º trimestre 1997', '2º trimestre 1997', '3º trimestre 1997', '4º trimestre 1997',
                  '1º trimestre 1998', '2º trimestre 1998', '3º trimestre 1998', '4º trimestre 1998',
                  '1º trimestre 1999', '2º trimestre 1999', '3º trimestre 1999', '4º trimestre 1999',
                  '1º trimestre 2000', '2º trimestre 2000', '3º trimestre 2000', '4º trimestre 2000',
                  '1º trimestre 2001', '2º trimestre 2001', '3º trimestre 2001', '4º trimestre 2001',
                  '1º trimestre 2002', '2º tri  mestre 2002', '3º trimestre 2002', '4º trimestre 2002',
                  '1º trimestre 2003', '2º trimestre 2003', '3º trimestre 2003', '4º trimestre 2003',
                  '1º trimestre 2004', '2º trimestre 2004', '3º trimestre 2004', '4º trimestre 2004',
                  '1º trimestre 2005', '2º trimestre 2005', '3º trimestre 2005', '4º trimestre 2005',
                  '1º trimestre 2006', '2º trimestre 2006', '3º trimestre 2006', '4º trimestre 2006',
                  '1º trimestre 2007', '2º trimestre 2007', '3º trimestre 2007', '4º trimestre 2007',
                  '1º trimestre 2008', '2º trimestre 2008', '3º trimestre 2008', '4º trimestre 2008',
                  '1º trimestre 2009', '2º trimestre 2009', '3º trimestre 2009', '4º trimestre 2009',
                  '1º trimestre 2010', '2º trimestre 2010', '3º trimestre 2010', '4º trimestre 2010',
                  '1º trimestre 2011', '2º trimestre 2011', '3º trimestre 2011', '4º trimestre 2011',
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
                  '1º trimestre 2024', '2º trimestre 2024', '3º trimestre 2024'],
    'Industria': [100.16, 97.3, 106.35, 100.08, 103.22, 105.13, 106.72, 106.49, 103.27, 104.8,
                  103.9, 100.75, 99.17, 100.18, 100.29, 102.23, 103.44, 104.31, 105.07, 106.69,
                  107.5, 105.11, 102.1, 102.02, 105.4, 107.89, 108.04, 111.26, 105.7, 106.1,
                  109.97, 111.26, 113.26, 115.69, 120, 119.82, 117.83, 121.86, 118.52, 120.02,
                  121.51, 119.64, 121.69, 125.11, 126.11, 130.03, 130.53, 131.53, 134.6, 136.64,
                  139.69, 128.6, 120.86, 125.78, 131.11, 136.42, 138.12, 141.89, 142.29, 144.43,
                  145.33, 149.19, 147.96, 147.55, 148.29, 144.55, 147.13, 145.88, 145.73, 151.24,
                  151.38, 150.15, 150.65, 146.15, 145.75, 146.87, 144.25, 139.46, 137.03, 134.6,
                  133.83, 134.12, 132.14, 129.82, 131.36, 131.08, 131.62, 133.14, 133.17, 132.44,
                  133.02, 132.39, 131.4, 131.8, 132, 132.3, 129.96, 114.46, 132, 135.41, 137.81,
                  135.47, 133.9, 130.45, 134.85, 136.75, 137.52, 136.65, 137.01, 137.88, 139.09,
                  140.92, 141.05, 143.33, 144.22]
}

# Criação do DataFrame das Despesas de Administração Pública
data_adm_publica = {
    'Trimestre': ['1º trimestre 1996', '2º trimestre 1996', '3º trimestre 1996', '4º trimestre 1996',
                  '1º trimestre 1997', '2º trimestre 1997', '3º trimestre 1997', '4º trimestre 1997',
                  '1º trimestre 1998', '2º trimestre 1998', '3º trimestre 1998', '4º trimestre 1998',
                  '1º trimestre 1999', '2º trimestre 1999', '3º trimestre 1999', '4º trimestre 1999',
                  '1º trimestre 2000', '2º trimestre 2000', '3º trimestre 2000', '4º trimestre 2000',
                  '1º trimestre 2001', '2º trimestre 2001', '3º trimestre 2001', '4º trimestre 2001',
                  '1º trimestre 2002', '2º trimestre 2002', '3º trimestre 2002', '4º trimestre 2002',
                  '1º trimestre 2003', '2º trimestre 2003', '3º trimestre 2003', '4º trimestre 2003',
                  '1º trimestre 2004', '2º trimestre 2004', '3º trimestre 2004', '4º trimestre 2004',
                  '1º trimestre 2005', '2º trimestre 2005', '3º trimestre 2005', '4º trimestre 2005',
                  '1º trimestre 2006', '2º trimestre 2006', '3º trimestre 2006', '4º trimestre 2006',
                  '1º trimestre 2007', '2º trimestre 2007', '3º trimestre 2007', '4º trimestre 2007',
                  '1º trimestre 2008', '2º trimestre 2008', '3º trimestre 2008', '4º trimestre 2008',
                  '1º trimestre 2009', '2º trimestre 2009', '3º trimestre 2009', '4º trimestre 2009',
                  '1º trimestre 2010', '2º trimestre 2010', '3º trimestre 2010', '4º trimestre 2010',
                  '1º trimestre 2011', '2º trimestre 2011', '3º trimestre 2011', '4º trimestre 2011',
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
                  '1º trimestre 2024', '2º trimestre 2024', '3º trimestre 2024'],
    'Despesas_Adm_Publica': [99.16, 100.76, 104.27, 88.51, 100.33, 99.93, 98.37, 99, 101.44, 102.12,
                             103.89, 103.04, 101.98, 103.09, 105.23, 107.12, 105.37, 104.37, 102.97,
                             104.04, 106.43, 106.63, 106.67, 107.9, 110.88, 110.92, 111.14, 110.99,
                             110.08, 111.17, 113.36, 116.31, 114.15, 118.3, 118.23, 117.73, 118.38,
                             119, 120.25, 120.21, 121.85, 121.89, 123.32, 127.84, 126.97, 130.03,
                             129.33, 128.67, 130.76, 130.59, 134.4, 129.82, 134.92, 133.32, 134.79,
                             137.97, 139.09, 139.94, 141.31, 141.82, 142.94, 144.33, 143.76, 143.44,
                             146.31, 147.16, 146.42, 147.73, 146.47, 148.79, 149.84, 151.42, 149.62,
                             150.59, 151.22, 149.96, 149.27, 148.1, 148.37, 147.06, 149.23, 148.8,
                             148.23, 147.86, 147.02, 147.29, 147.13, 148.66, 148.58, 148.96, 149.57,
                             147.58, 148.22, 148.11, 147.81, 147.64, 148.29, 136.26, 141.15, 144.27,
                             145.49, 147.38, 149.64, 151.23, 151.28, 150.08, 153.45, 151.65, 153.58,
                             157.45, 158.7, 159.64, 159.75, 159.34, 160.59]
}

# Criação do DataFrame das Despesas de Administração Pública
df_adm_publica = pd.DataFrame(data_adm_publica)

# Aplicando o logaritmo natural às Despesas de Administração Pública
df_adm_publica['log_Despesas_Adm_Publica'] = np.log(df_adm_publica['Despesas_Adm_Publica'])

# Aplicando o filtro Hodrick-Prescott às Despesas de Administração Pública
cycle_adm_publica, trend_adm_publica = hpfilter(df_adm_publica['log_Despesas_Adm_Publica'], lamb=1600)

# Adicionando as séries de tendência e cíclica ao DataFrame das Despesas de Administração Pública
df_adm_publica['Trend'] = trend_adm_publica
df_adm_publica['Cycle'] = cycle_adm_publica

# Criação do DataFrame da Indústria
df_industria = pd.DataFrame(data_industria)

# Aplicando o logaritmo natural à Indústria
df_industria['log_Industria'] = np.log(df_industria['Industria'])

# Aplicando o filtro Hodrick-Prescott à Indústria
cycle_industria, trend_industria = hpfilter(df_industria['log_Industria'], lamb=1600)

# Adicionando as séries de tendência e cíclica ao DataFrame da Indústria
df_industria['Trend'] = trend_industria
df_industria['Cycle'] = cycle_industria

# Gráfico do PIB e sua tendência
plt.figure(figsize=(12, 6))
plt.plot(df_pib['Trimestre'], df_pib['log_PIB'], label='Log PIB', marker='o')
plt.plot(df_pib['Trimestre'], df_pib['Trend'], label='Tendência (Filtro HP)', color='red')
plt.title('Log do PIB e Tendência (Filtro Hodrick-Prescott)')
plt.xlabel('Trimestre')
plt.ylabel('Log do PIB')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Gráfico das Despesas de Consumo e sua tendência
plt.figure(figsize=(12, 6))
plt.plot(df_consumo['Trimestre'], df_consumo['log_Despesas_Consumo'], label='Log Despesas de Consumo', marker='o')
plt.plot(df_consumo['Trimestre'], df_consumo['Trend'], label='Tendência (Filtro HP)', color='red')
plt.title('Log das Despesas de Consumo e Tendência (Filtro Hodrick-Prescott)')
plt.xlabel('Trimestre')
plt.ylabel('Log das Despesas de Consumo')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Gráfico da Formação Bruta de Capital e sua tendência
plt.figure(figsize=(12, 6))
plt.plot(data_investimento['Trimestre'], np.log(data_investimento['Formacao_Capital']), label='Log Formação de Capital', marker='o')
trend_investimento = hpfilter(np.log(data_investimento['Formacao_Capital']), lamb=1600)[1]
plt.plot(data_investimento['Trimestre'], trend_investimento, label='Tendência (Filtro HP)', color='red')
plt.title('Log da Formação Bruta de Capital e Tendência (Filtro Hodrick-Prescott)')
plt.xlabel('Trimestre')
plt.ylabel('Log da Formação Bruta de Capital')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Gráfico das Despesas de Administração Pública e sua tendência
plt.figure(figsize=(12, 6))
plt.plot(df_adm_publica['Trimestre'], df_adm_publica['log_Despesas_Adm_Publica'], label='Log Despesas Adm Pública', marker='o')
plt.plot(df_adm_publica['Trimestre'], df_adm_publica['Trend'], label='Tendência (Filtro HP)', color='red')
plt.title('Log das Despesas de Administração Pública e Tendência (Filtro Hodrick-Prescott)')
plt.xlabel('Trimestre')
plt.ylabel('Log das Despesas de Administração Pública')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Gráfico da Indústria e sua tendência
plt.figure(figsize=(12, 6))
plt.plot(df_industria['Trimestre'], df_industria['log_Industria'], label='Log Indústria', marker='o')
plt.plot(df_industria['Trimestre'], df_industria['Trend'], label='Tendência (Filtro HP)', color='red')
plt.title('Log da Indústria e Tendência (Filtro Hodrick-Prescott)')
plt.xlabel('Trimestre')
plt.ylabel('Log da Indústria')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Gráfico do PIB e seu componente cíclico
plt.figure(figsize=(12, 6))
plt.plot(df_pib['Trimestre'], df_pib['Cycle'], label='Componente Cíclico do PIB', color='blue')
plt.title('Componente Cíclico do PIB')
plt.xlabel('Trimestre')
plt.ylabel('Ciclo do PIB')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()

# Gráfico das Despesas de Consumo e seu componente cíclico
plt.figure(figsize=(12, 6))
plt.plot(df_consumo['Trimestre'], df_consumo['Cycle'], label='Componente Cíclico das Despesas de Consumo', color='green')
plt.title('Componente Cíclico das Despesas de Consumo')
plt.xlabel('Trimestre')
plt.ylabel('Ciclo das Despesas de Consumo')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()

# Gráfico da Formação Bruta de Capital e seu componente cíclico
plt.figure(figsize=(12, 6))
plt.plot(data_investimento['Trimestre'], trend_investimento - np.log(data_investimento['Formacao_Capital']), 
         label='Componente Cíclico da Formação Bruta de Capital', color='orange')
plt.title('Componente Cíclico da Formação Bruta de Capital')
plt.xlabel('Trimestre')
plt.ylabel('Ciclo da Formação Bruta de Capital')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()

# Gráfico das Despesas de Administração Pública e seu componente cíclico
plt.figure(figsize=(12, 6))
plt.plot(df_adm_publica['Trimestre'], df_adm_publica['Cycle'], label='Componente Cíclico das Despesas Adm Pública', color='purple')
plt.title('Componente Cíclico das Despesas de Administração Pública')
plt.xlabel('Trimestre')
plt.ylabel('Ciclo das Despesas de Administração Pública')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()

# Gráfico da Indústria e seu componente cíclico
plt.figure(figsize=(12, 6))
plt.plot(df_industria['Trimestre'], df_industria['Cycle'], label='Componente Cíclico da Indústria', color='red')
plt.title('Componente Cíclico da Indústria')
plt.xlabel('Trimestre')
plt.ylabel('Ciclo da Indústria')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()


# Gráficos de dispersão para cada componente cíclico em relação ao ciclo do PIB
# Ciclo de Consumo
plt.figure(figsize=(10, 6))
plt.scatter(df_consumo['Cycle'], df_pib['Cycle'], color='blue', label='Ciclo de Consumo')
plt.xlabel('Ciclo de Consumo')
plt.ylabel('Ciclo do PIB')
plt.title('Dispersão entre Ciclo de Consumo e Ciclo do PIB')
# Estimando a linha de tendência
m_consumo, b_consumo = np.polyfit(df_consumo['Cycle'], df_pib['Cycle'], 1)
plt.plot(df_consumo['Cycle'], m_consumo * df_consumo['Cycle'] + b_consumo, color='red')
plt.legend()
plt.grid()
plt.show()
# Ciclo de Investimento
plt.figure(figsize=(10, 6))
plt.scatter(df_investimento['Cycle'], df_pib['Cycle'], color='green', label='Ciclo de Investimento')
plt.xlabel('Ciclo de Investimento')
plt.ylabel('Ciclo do PIB')
plt.title('Dispersão entre Ciclo de Investimento e Ciclo do PIB')
# Estimando a linha de tendência
m_investimento, b_investimento = np.polyfit(df_investimento['Cycle'], df_pib['Cycle'], 1)
plt.plot(df_investimento['Cycle'], m_investimento * df_investimento['Cycle'] + b_investimento, color='red')
plt.legend()
plt.grid()
plt.show()
# Ciclo da Indústria
plt.figure(figsize=(10, 6))
plt.scatter(df_industria['Cycle'], df_pib['Cycle'], color='orange', label='Ciclo da Indústria')
plt.xlabel('Ciclo da Indústria')
plt.ylabel('Ciclo do PIB')
plt.title('Dispersão entre Ciclo da Indústria e Ciclo do PIB')
# Estimando a linha de tendência
m_industria, b_industria = np.polyfit(df_industria['Cycle'], df_pib['Cycle'], 1)
plt.plot(df_industria['Cycle'], m_industria * df_industria['Cycle'] + b_industria, color='red')
plt.legend()
plt.grid()
plt.show()
# Ciclo da Administração Pública
plt.figure(figsize=(10, 6))
plt.scatter(df_adm_publica['Cycle'], df_pib['Cycle'], color='purple', label='Ciclo da Adm Pública')
plt.xlabel('Ciclo da Adm Pública')
plt.ylabel('Ciclo do PIB')
plt.title('Dispersão entre Ciclo da Adm Pública e Ciclo do PIB')
# Estimando a linha de tendência
m_adm_publica, b_adm_publica = np.polyfit(df_adm_publica['Cycle'], df_pib['Cycle'], 1)
plt.plot(df_adm_publica['Cycle'], m_adm_publica * df_adm_publica['Cycle'] + b_adm_publica, color='red')
plt.legend()
plt.grid()
plt.show()
# Estatísticas
correlation_consumo = df_consumo['Cycle'].corr(df_pib['Cycle'])
correlation_investimento = df_investimento['Cycle'].corr(df_pib['Cycle'])
correlation_industria = df_industria['Cycle'].corr(df_pib['Cycle'])
correlation_adm_publica = df_adm_publica['Cycle'].corr(df_pib['Cycle'])
std_ciclo_consumo = df_consumo['Cycle'].std()
std_ciclo_investimento = df_investimento['Cycle'].std()
std_ciclo_industria = df_industria['Cycle'].std()
std_ciclo_adm_publica = df_adm_publica['Cycle'].std()
std_ciclo_pib = df_pib['Cycle'].std()
# Exibindo os resultados
print(f'Correlação Ciclo de Consumo com Ciclo do PIB: {correlation_consumo}')
print(f'Correlação Ciclo de Investimento com Ciclo do PIB: {correlation_investimento}')
print(f'Correlação Ciclo da Indústria com Ciclo do PIB: {correlation_industria}')
print(f'Correlação Ciclo da Adm Pública com Ciclo do PIB: {correlation_adm_publica}')
print(f'Desvio Padrão Ciclo de Consumo: {std_ciclo_consumo}')
print(f'Desvio Padrão Ciclo de Investimento: {std_ciclo_investimento}')
print(f'Desvio Padrão Ciclo da Indústria: {std_ciclo_industria}')
print(f'Desvio Padrão Ciclo de Adm Pública: {std_ciclo_adm_publica}')
print(f'Desvio Padrão Ciclo do PIB: {std_ciclo_pib}')