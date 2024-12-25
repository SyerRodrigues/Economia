install.packages('BatchGetSymbols')
install.packages('tidyverse')
install.packages('fPortfolio')

#chamando as bibliotecas
library(tidyverse)
library(ggplot2)
library(BatchGetSymbols)
library(fPortfolio)


# set dates
first.date <- as.Date('2015-01-01')
last.date <- Sys.Date()
freq.data <- 'weekly'

#ações
tickers <- c('BBDC4.SA','IGTA3.SA','PETR4.SA','CYRE3.SA')

l.out <- BatchGetSymbols(tickers = tickers, 
                         first.date = first.date,
                         last.date = last.date, 
                         freq.data = freq.data,
                         cache.folder = file.path(tempdir(), 
                                                  'BGS_Cache') )

#gráficos
p <- ggplot(l.out$df.tickers, aes(x = ref.date, y = price.close))
p <- p + geom_line()
p <- p + facet_wrap(~ticker, scales = 'free_y') 
print(p)


# Filtrando os retornos Bradesco
bradesco <- l.out$df.tickers %>% 
  na.omit() %>% 
  filter(ticker == 'BBDC4.SA') %>% 
  select( ret.closing.prices) %>% 
  rename( Bradesco = ret.closing.prices) #Observe que modificamos o nome da coluna.


#Filtrando os retornos da Cyrela
cyrela <- l.out$df.tickers %>% 
  na.omit() %>% 
  filter(ticker == 'CYRE3.SA') %>% 
  select( ret.closing.prices) %>% 
  rename(Cyrela = ret.closing.prices) #Observe que modificamos o nome da coluna.

#Filtrando os retornos da Petrobras
petrobras <- l.out$df.tickers %>% 
  na.omit() %>% 
  filter(ticker == 'PETR4.SA') %>% 
  select( ret.closing.prices) %>% 
  rename(Petrobras = ret.closing.prices) #Observe que modificamos o nome da coluna.


#Criando os uma variável com todos os retornos
retornos <- cbind(bradesco,cyrela,petrobras)
retornos


cor(bradesco, cyrela)

#Transformando os retornos em séries de tempo
retornos <- as.timeSeries(retornos)

# Portfolio com a melhor relação entre risco/retorno
portfolio.eficiente <- tangencyPortfolio(retornos, spec = portfolioSpec(), constraints = "LongOnly")
portfolio.eficiente


# Portfolio com menor risco:
portfolio.menor.risco <- minvariancePortfolio(retornos,spec = portfolioSpec(), constraints = "LongOnly")
portfolio.menor.risco


## Obtenção da fronteira
fronteira <- portfolioFrontier(retornos)

# Gráfico com a fronteira eficiente
frontierPlot(fronteira, col = c('blue', 'red'), pch = 20)

## Adicionando informações no gráfico
monteCarloPoints(fronteira, mcSteps = 5000, pch = 20, cex = 0.25 )


