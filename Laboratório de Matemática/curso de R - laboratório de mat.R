#Aula 1 - R
#Funções e variáveis


#getwd()
#setwd("C:\\Users\\syerf\\OneDrive\\Área de Trabalho\\Syer Filho\\ufpe\\contabilidade social")
a <- 3.6
b <- sqrt(35)
d <- -2.1

a
b
d

aa <-  2*a+b - d
aa
round(aa,2) #arredondar

bb <- a*b/d
bb
round(bb,2)


#mean, var, sd, min, range, sum 
#sum= somatório
#mean = média


b = c(1,15,18,3,6)
b

mean(b)


#cumsum(), sort(), diff()
#támbem operam sobre todo o vertor



#mais usuais: sqrt() = raiz; abs()= valor absoluto; exp() = exponencial;
#log10(); log()= na base e; factorial(); choose()= número de conbinações; gamma()



# array contêm um só tipo de objetos
#vector = one dimensional array
#matrix = two dimensional array
#list é  uma coleção ordenada de objectos
#data frames

############ área x riqueza #######################
area <- c(303, 379, 961, 295, 332, 47, 122, 11, 53, 2479)
riqueza <- c(3, 10, 20, 7, 8, 4, 8, 3, 5, 23)

area
riqueza

bb<- riqueza/area
bb

#regressão linear - linear model
modelo1 <- lm(riqueza~area) #~ = função
modelo1
summary(modelo1)

plot(modelo1)


### Exercício: Calcular as seguintes equações -
# a) Altura dos Homens: 1,67; 2,00; 1,90; 1,74; 1,65;
# b) Altura das mulheres: 1,54; 1,67; 1,78; 1,87; 1,63;
# c) utilizar a funçãp tapply() para calcular a média das alturas, valores  máximos, mínimos, variâcia.

homens = c(1.67,2.0, 1.9, 1.74, 1.65)
mulheres = c(1.54, 1.67, 1.78, 1.87, 1.63)

alturas <- c(homens, mulheres)
tapply(homens)
tapply(mulheres)

medias <- tapply(alturas)

# Passo 1: Criação dos vetores
homens <- c(1.67, 2.0, 1.9, 1.74, 1.65)
mulheres <- c(1.54, 1.67, 1.78, 1.87, 1.63)

# Combinação dos vetores em um só vetor de alturas
alturas <- c(homens, mulheres)

# Passo 2: Criação do vetor de fatores
genero <- factor(c(rep("homem", length(homens)), rep("mulher", length(mulheres))))

# Passo 3: Uso do tapply para calcular a média das alturas por gênero
medias <- tapply(alturas, genero, mean)

# Exibir o resultado
print(medias)


###Aplicações em R - matemática financeira##

#Ex1:
tx.de.juros<-0.05
cap.inicial<-1000
prazo<-10
cap.final<-cap.inicial*(1+tx.de.juros)^prazo
cap.final


#Ex2:

tx.de.juros<- c(4.5,5.1,4,3.6,3,5,4.6,4.8,3.6,5)/100
saldos<- c(10,150,45,20,100,75,15,67,9,2)*1000
juros<- saldos*tx.de.juros
cap.final<- saldos*(c(1,1,1,1,1,1,1,1,1,1) + tx.de.juros)^5
cap.final



##########################################################################################

#Aula 2

serie <- rnorm(1000, 100, 50)#rnorm = aleatorio (Qtd, mean, desviopadrao)
serie

serie1 <- sort(serie) #ordena, "decrase = true"
serie1
min(serie1)

serie2 <- round(serie1,2) #round = (arredondar, núm casa decimais)
serie2

#s<- rnorm(10)
#s

#serie3 <- summary(serie2)
#serie3

diferenca <- mean(serie[1:500]) - mean(serie[501:1000]) #essa dif tende a zero
diferenca

media_menor <- mean(serie[1:100])
round(media_menor, 2)

media_maior<- mean(serie[901:1000])
round(media_maior, 2)

cc <- function(cap, txj, prazo){
				resultado <- cap*(1+txj)^prazo
				resultado
}

cc(1000,0.50,30)
#testando a função
#cap1 <- c(1000, 2000, 3000)
#cap1
#cc(cap1, 0.05, 30)

cap2 <- c(10000,20000,60000)

cc1<-function(cap, txj, prazo){
		if(cap>50000){
			txj<-txj+0.005}
		else{
			txj<-txj}
		resultado<-cap*(1+txj)^prazo
		resultado
}

cc1(4000,0.10, 5)
cc1(cap2,0.005,5)
resultado2 <- cc1(cap2, 0.005, 5)
print(resultado2)
#Função demanda partida

#se afunção 0<=x<=100; y1 = 1000-0.20*x
#se afunção 101<=x<=200; y1 = 1050-0.21*x
#se afunção 200<=x<=300; y1 = 1090-0.22*x

x<- 1:100
y1<-1000-0.20*x
y1
plot(y1)

x<-101:200)
y2 <- 1050-0.21*x
y2
plot(y2)

x<-201:300
y3<-1090-0.22*x
plot(y3)

yfinal <- c(y1, y2, y3)
yfinal
plot(yfinal)


library(ggplot2)

# Criação dos vetores de dados
x1 <- 1:100
y1 <- 1000 - 0.20 * x1

x2 <- 101:200
y2 <- 1050 - 0.21 * x2

x3 <- 201:300
y3 <- 1090 - 0.22 * x3

# Combinação dos dados em um único dataframe
x <- c(x1, x2, x3)
y <- c(y1, y2, y3)

data <- data.frame(x = x, y = y)

# Criação do gráfico com ggplot2
#ggplot(data, aes(x = x, y = y)) +
 # geom_line(color = "blue", size = 1) +  # Adiciona a linha
  #geom_point(color = "red", size = 2) +  # Adiciona pontos
  #labs(title = "Gráfico de y vs. x",
   #    x = "X",
    #y = "Y") +  # Adiciona títulos e rótulos dos eixos
  #theme_minimal() +  # Define o tema do gráfico
  #theme(
    #plot.title = element_text(hjust = 0.5, size = 20),  # Centraliza o título e ajusta o tamanho
    #axis.title.x = element_text(size = 15),  # Ajusta o tamanho do rótulo do eixo x
    #axis.title.y = element_text(size = 15)   # Ajusta o tamanho do rótulo do eixo y
  #)

###########################################################################################
cap2 <- c(10000,20000,60000)
cc1 <- function(cap, txj, prazo) {
  sapply(cap, function(c) {
    if (c > 50000) {
      txj <- txj + 0.005
    }
    resultado <- c * (1 + txj) ^ prazo
    resultado
  })
}

# Teste da função com um valor único
resultado1 <- cc1(4000, 0.10, 5)
resultado1

resultado2 <- cc1(cap2, 0.005, 5)
resultado2






#######################################################################################################
###### Aula 3 - 17/06/2024

#media 0.20 desvio 0.20 
#media 0.21 desvio 0.20
#media 0.22 desvio 0.20


alea1 <- rnorm(100, 0.20, 0.2) #coeficiente angular da reta com média 20 com desvio padrão de 0.20
alea1
alea2 <- rnorm(100, 0.21, 0.2)
alea2
alea3 <- rnorm(100, 0.22, 0.2)
alea3


x<- 1:100
y1 <- (1000-alea1*x)
y1
y11 <- sort(y1, decreasing=T)

x<- 101:200
y2<- (1050-alea2*x)
y2
y22 <- sort(y2, decreasing=T)

x<- 201:300
y3<- (1090-alea3*x)
y3
y33<- sort(y3, decreasing=T)

y<- c(y1, y2, y3)
y<- c(y11, y22, y33)
plot(y)

hist(alea1, col=7)
hist(alea2, col=2)
hist(alea3, col=3)


y1=0
y2=0
y3=0
y4=0
y=0

for(i in 1:500){y1[i]<-1000}
for(i in 1:500){y2[i]<- 500}
for(i in 1:500){y3[i]<- 200}
for(i in 1:500){y4[i] <- 100}

y<- c(y1, y2, y3, y4)
plot(y)




###############################################################################################
####Aula 4 - 20/06/24####

#matrizes -> formas de escrever

matrix(c(1,5,38,400),2,2)#nesse caso é um vetor, porém pode ser um data frame e etc
matrix((1:6), 2,3, byrow=TRUE) #matriz vai ser preenchida pelas linhas
matrix(rnorm(9),3,3)
matrix(c("a", "b", "c", "d"), 2, 2)

matriz2 <- matrix(c(1,1,1,2,2,2),2,3, byrow=TRUE)
colnames(matriz2)<-c("Idade", "altura", "pcd") #nome colunas
rownames(matriz2)<- c("num1", "metro")
matriz2

iptu = 0.20
iptu
###matriz iptu###
matriziptu <- matriz2*iptu
colnames(matriz2)<-c("flat", "apartamento", "casa") #nome colunas
rownames(matriz2)<- c("homem", "mulher")
matriziptu


#multiplicação element p/elemento "*"
#multiplicação matricial A%*%B # regra tem q ser valida
t(A) #transposta de a

#solve(A) #matriz inversa de A
#solve(A, b) #devolve o vetor x na equação b = Ax



########### aula 5 - 27/06 ############### 

#1 -> Selecionar valores de um vetor  que sejam maiores do que 3, dado: 

x1<-c(1,3,5,4,7,9,2,4.5,10)
x1
## para selecionar os valores maiores que 3 
x2<-x1[x1>3] ## barras indicando posição 
x2


#2 -> Selecionar valores onde x>3 e menores do que 9 

x3<-x1[(x1>3)&(x1<9)] # mais outro "& "
print(x3)

#3 -> "ou = |" Selecionar valores menores do que 3 ou maiores do que 9 
x4<-x1[(x1<3)|(x1>9)]
print(x4)

#4 -> Sejam: set x5 e x6 ## criando vetor x4 e x5
x5<-c(1,4,6,8,12)
x6<-c(-2,-3,4,10,14) 

## encontrar elementos de x5 utilizando x6 como critérios, nesse caso sendo x6 positivos 
x7<-x5[x6>0]
x7 ### maneira de metrificar causalidades, uma maneira manual de correlação 

##############

set.seed(1357532)# Define sementes(dados originais) aleatórias para reprodutibilidade, sem relação. Máxima geração de números independentes.

N<-1000 # especificando o tamanho da amostra 
y<-rnorm(N,2,3)
y
 
#### criando variáveis aleatórias #####

x1<-rnorm(N)
x1
x2<-runif(N)+0.25*x1 ### x2 25% dependente de x1
x2
x3<-rpois(N,3)-0.3*x1+0.5*x2
x3
y<-rnorm(N,2,3)+5*x1+2*x2+0.5*x3
y
x1
x2
x3
y

#rnorm é uma gaussiana 
# rpois pode ser com assimetria positiva ou negativa e uma linear 

# 1-> elaborar matriz de correlação entre as variáveis 

d<-cor(x1,x2)
b<-cor(x1,x3)
h<-cor(x1,y)
j<-cor(x2,x3)# cor(y,x1)
k<-cor(x2,y)
l<-cor(x3,y)
# 2-> ##### matriz de correlação 
matrizcorr<-matrix(c(1,d,b,h,d,1,j,k,b,j,1,l,h,k,l,1),4,4,byrow=TRUE)
colnames(matrizcorr)<-c("x1","x2","x3","y")
rownames(matrizcorr)<-c("x1","x2","x3","y")
matrizcorr

# 3-> ##### calcular y = f(x1,x2,x3)
ylm<-lm(y~x1+x2+x3)
summary(ylm)

# 4-> ####### 

x1<- 1; x2<- 1; x3<- 1 # p (1,1,1)
y2<- 1.89 + 5 * x1 + 2.29 * x2 + 0.49 * x3
y2
x1<- 10; x2<- 10; x3<- 10 # p(10,10,10)
y3<- 1.89 + 5 * x1 + 2.29 * x2 + 0.49 * x3
y3
x1<- 100; x2<- 100; x3<- 100 # p (100, 100, 100)
y4<- 1.89 + 5 * x1 + 2.29 * x2 + 0.49 * x3
y4

#5. #######

y1<- log(y)
y1


##################Aula 6 01/07/2024###################

#Resolver sistemas de equações lineares
#Resolver sistemas, imaginemos o seguinte sistemas de equações:
#'Sistemas Lineares

#-4x + 0.3y = 12.3 (1)
#54.3x - 4y = 45  (2)

#podemos resolvê-lo em R da seguinte forma:

coefs <- matrix(c(-4, 0.3, 54.3, -4), 2, 2, byrow = T)
coefs
ys <- c(12.3, 45)
ys

solve(coefs, ys)
ys[1]
ys[2]

'Trabalhando com gráficos'

#exemplo 1

a <- 1:20
b <- a^2
plot(a,b,col ="red")

#exemplo 2

a <- 1:20
b <- a^2
plot(a,b,type = "l", col ="red")

#exemplo 3

a <- 1:20
b <- a^2
plot(a,b, col ="red")
lines(rev(a), b, col="blue") #adição de linhas / reverso de a
points(a, 400-b, col="green") #adição de pontos / mudança no próprio gráfico

#exemplo 4

a<- 1:20; b <- a^2
plot(a, b, pch=2)#tipo de símbolos
points(a, 400-b, pch=5)
points(a, 200-b, pch=10)
plot(0:20, 0:20, pch=0:20)

#exemplo 5

a<- 1:20; b <- a^2
plot(a, b, type="l", col="green")
lines(a,2*b,lwd"=4,col="red")#espessura
lines(a, 0.5*b, lty=2, col="blue") #estilo
lines(a,3*b, lty=3, col="brown")


#exemplo 6

x<- 0:20
y<- x^3
plot(c(0,20),c(-8000, 8000), type= "n",xlab=NA, ylab=NA)
lines(x,y, col="blue")
lines(x, -y, col="red")
title("Gráfico de duas funções", xlab="valores de x", ylab="valores de y")


#exemplo 7:
#duas séries

ano<- 2001:2009
tri1<- c(72.8, 66.2, 69.2, 65.9, 62.4, 67.8, 61.3, 68.5, 70.4)
tri2<- c(60.6, 53.7, 55.3, 56.7, 56.4, 57.8, 57.5, 59.8, 63.3)
plot(ano, tri1, type="l", main="taxa de ocupação por trimesre dos hotéis - município do Rio de Janeiro", xlab= "ano", ylab= "Taxa de ocupação %", col="blue", ylim=c(50,80))
lines(ano, tri2, col="red")

# Regressão linear com gráficos -> ver tendências

x = c(72.8, 66.2, 69.2, 65.9, 62.4, 67.8, 61.3, 68.5, 70.4)
y<-c(72.8, 66.2, 69.2, 65.9, 62.4, 67.8, 61.3, 68.5, 70.4)

plot(x, y) #gráfico
abline(lm(y ~ x)) #gráfico da regressão linear
'ou'
lm(y~x) #regressão y com x
lm(formula = y ~ x)
lm[[1]][1]

lmregress<- lm(y~x)
summary(lmregress)
lmregress[[1]][1]
lmregress[[1]][2]



###########################Aula 7 - 04/07/2024##################################
'utilizando o resultado para resolver a questão indicada abaixo:'
'Calcular o valor de z = 2*x +300*y'
z <- 2*lmregress[[1]][1] + 300*lmregress[[1]][2] #redefinindo a função
z


###exemplo 9:
'Através do parâmetro "plot.type" podemos indicar que pretendemos um só gráfico com todas as series'
m <- ts(matrix(rnorm(300), 100, 3), start=c(1961,6), frequency = 12) #ts = series temporais
m

plot(m, plot.tyoe ="single", col =1:3)
legend("topright", legend = colnames(m), col = 1:3, lty = 1)


#Puxando dados

#Verificar o diretório de trabalho atual
getwd()

#Mudar para o diretório correto (certifique-se de que o caminho está correto)
setwd("C:/Users/syerf/OneDrive/Documentos/estudos python/data science/streamlit")

#Carregar a biblioteca xlsx
library('xlsx')

#Ler o arquivo Excel (certifique-se de que o arquivo existe no diretório)
dados <- read.xlsx("database_eleicoes.xlsx", sheetIndex = 1)

#Anexar e resumir os dados
attach(dados)
summary(dados)
dados

#########Aula 8 - 08/07/2024##################

#Série de taylor -> simplifica= é de grande importância para o estudo de métodos numéricos por fornecer um meio de aproximar uma função f(x)
#isso nos perimite manipular polinômio

#utilizar os comandos de laços

#a) y(x)= e^x*sen(x)
#b) y(x) = e^x *cos(x)
#c) Y(x) = 28e^x+ e^-x
#d) imprimir o polinômio encontrado
#e) elaborar os gráficos das funções acima



### Gráficos Especiais -> 1

set.seed(1234)
n<- 10000
c1<- matrix(rnorm(n, mean=0, sd=.5), ncol=4)
c1

c2<-matrix(rnorm(n,mean=3, sd=2), ncol=4)
c2

mydata <- rbind(c1, c2)
mydata
mydata <- as.data.frame(mydata)
mydata
mydata <- as.data.frame(mydata)
names(mydata)<- c("x", "y")
mydata
with(mydata,
plot(x, y, pch=19, main="Scatter plot with 10.000 observations"))

with(mydata,
smoothScatter(x, y, pch=19, main="Scatter plot with 10.000 observations"))

#####Gráficos especiais - 2


install.packages("hexbin")
library(hexbin)

with(mydata, {
bin<- hexbin(x, y, xbins=50)
plot(bin, main="hexagonal Binning with 10.000 observation")
})


####Gráficos especiais - 3 
install.packages("scatterplot3d")
library(scatterplot3d)
mtcars
attach(mtcars)
scatterplot3d(wt, disp, mpg,
main="Basic 3D Scatter Plot")


###Gráficos Especiais - 4
library(scatterplot3d)
mtcars
attach(mtcars)
scatterplot3d(wt, disp, mpg,
pch=16,
highlight.3d=TRUE,
type="h",
main="Basic 3D Scatter Plot")

#Mudar para o Script do GGPLOT - Gráficos especiais - como trabalhar



install.packages("ggplot2")
library(ggplot2)
head(mtcars)

g <- ggplot(mtcars)
#Prepara área de gráficos 
#adicionar pontos(geom_point)
g <- g + geom_point(aes(x = hp, y = mpg, color = factor(am)),
size =3)
g

# am - binário, se o carro é automático ou manual

#altera a escala de cores

g <- g + 
	scale_color_manual("Automatic",
					values = c("red", "blue"),
					labels = c("No", "Yes"))
g

#Rótulos (títulos)

g <- g +
	labs(title ='Relação entre consumo, potência e tipo de câmbio',
	y = 'Consumo',
	x = 'Potência')
g

#Gráfico poderia ser criado com um bloco único de código:

ggplot(mtcars) +
	geom_point(aes(,x = hp, y = mpg, color = factor(am))
	scale_color_manual("Automatic",
					values = c("red", "blue"),
					labels = c("No", "Yes"))
	labs(title ='Relação entre consumo, potência e tipo de câmbio',
	y = 'Consumo',
	x = 'Potência')
g

	


# Carteira Markovisk

#retira diretamente do Yahoo finance, Google finance
