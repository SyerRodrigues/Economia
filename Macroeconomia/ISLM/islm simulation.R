### Lista 1 - Macro 1 - Quest�o  9 ###
# Definindo os par�metros do modelo
c0 <- 100
c1 <- 0.8
c2 <- 0.3
A <- 400
a <- 0.8
rho <- 0.9

# Par�metros para a simula��o
G_bar <- 100  # Gasto do governo
T_bar <- 100  # Impostos
r_bar <- 0.1075  # Taxa de juros ex�gena (10.75%)
T <- 40  # N�mero de per�odos

# Inicializa��o das vari�veis
Y0 <- numeric(T)  # Produto sem choque
C0 <- numeric(T)  # Consumo sem choque
I0 <- numeric(T)  # Investimento sem choque
Tt <- rep(T_bar, T)  # Impostos
Gt <- rep(G_bar, T)  # Gastos do governo
rt <- rep(r_bar, T)  # Taxa de juros

# Fun��o para calcular Yt
calcular_Y <- function(Ct, It, Gt) {
  return(Ct + It + Gt)
}

# Fun��o para calcular Ct
calcular_C <- function(Yt, Tt, rt) {
  return(c0 + c1 * (Yt - Tt) - c2 * rt)
}

# Fun��o para calcular It
calcular_I <- function(rt) {
  return(A - a * rt)
}

# Fun��o de Impulso Resposta Generalizada (GIRF)
calcular_GIRF <- function(x1, x0) {
  return(((x1 - x0) / x0) * 100)
}

# Simula��o sem mudan�as nas pol�ticas (vari�veis base)
for (t in 2:T) {
  C0[t] <- calcular_C(Y0[t-1], Tt[t], rt[t])
  I0[t] <- calcular_I(rt[t])
  Y0[t] <- calcular_Y(C0[t], I0[t], Gt[t])
}

# Simula��o com choque de 1% em Gt no tempo t=2 (Pol�tica Fiscal Expansionista)
Gt_choque <- Gt
Gt_choque[2] <- Gt_choque[2] * 1.01  # Aumento de 1% em Gt

# Recalcular as vari�veis com o choque fiscal
Y_fiscal <- numeric(T)
C_fiscal <- numeric(T)
I_fiscal <- numeric(T)
Y_fiscal[1] <- Y0[1]  # Valor inicial igual ao original
for (t in 2:T) {
  C_fiscal[t] <- calcular_C(Y_fiscal[t-1], Tt[t], rt[t])
  I_fiscal[t] <- calcular_I(rt[t])
  Y_fiscal[t] <- calcular_Y(C_fiscal[t], I_fiscal[t], Gt_choque[t])
}

# Simula��o com choque de 1% em r_t no tempo t=2 (Pol�tica Monet�ria Expansionista)
rt_choque <- rt
rt_choque[2] <- rt_choque[2] * 0.99  # Redu��o de 1% na taxa de juros

# Recalcular as vari�veis com o choque monet�rio
Y_monetario <- numeric(T)
C_monetario <- numeric(T)
I_monetario <- numeric(T)
Y_monetario[1] <- Y0[1]  # Valor inicial igual ao original
for (t in 2:T) {
  C_monetario[t] <- calcular_C(Y_monetario[t-1], Tt[t], rt_choque[t])
  I_monetario[t] <- calcular_I(rt_choque[t])
  Y_monetario[t] <- calcular_Y(C_monetario[t], I_monetario[t], Gt[t])
}

# Simula��o com choque de 1% em T_t no tempo t=2 (Redu��o de Impostos)
Tt_choque <- Tt
Tt_choque[2] <- Tt_choque[2] * 0.99  # Redu��o de 1% em Tt

# Recalcular as vari�veis com o choque de impostos
Y_impostos <- numeric(T)
C_impostos <- numeric(T)
I_impostos <- numeric(T)
Y_impostos[1] <- Y0[1]  # Valor inicial igual ao original
for (t in 2:T) {
  C_impostos[t] <- calcular_C(Y_impostos[t-1], Tt_choque[t], rt[t])
  I_impostos[t] <- calcular_I(rt[t])
  Y_impostos[t] <- calcular_Y(C_impostos[t], I_impostos[t], Gt[t])
}

# Calcular as GIRFs para cada cen�rio
GIRF_Y_fiscal <- calcular_GIRF(Y_fiscal, Y0)
GIRF_C_fiscal <- calcular_GIRF(C_fiscal, C0)
GIRF_I_fiscal <- calcular_GIRF(I_fiscal, I0)
GIRF_G_fiscal <- calcular_GIRF(Gt_choque, Gt)

GIRF_Y_monetario <- calcular_GIRF(Y_monetario, Y0)
GIRF_C_monetario <- calcular_GIRF(C_monetario, C0)
GIRF_I_monetario <- calcular_GIRF(I_monetario, I0)
GIRF_r_monetario <- calcular_GIRF(rt_choque, rt)

GIRF_Y_impostos <- calcular_GIRF(Y_impostos, Y0)
GIRF_C_impostos <- calcular_GIRF(C_impostos, C0)
GIRF_I_impostos <- calcular_GIRF(I_impostos, I0)
GIRF_T_impostos <- calcular_GIRF(Tt_choque, Tt)

# Plotando os resultados
par(mfrow=c(3,3), mar=c(3,4,3,2))

# Gr�ficos para pol�tica fiscal expansionista (aumento de Gt)
plot(1:T, GIRF_Y_fiscal, type="l", main="GIRF - Y (Fiscal Expansionista)", xlab="Per�odo", ylab="GIRF (%)")
plot(1:T, GIRF_C_fiscal, type="l", main="GIRF - C (Fiscal Expansionista)", xlab="Per�odo", ylab="GIRF (%)")
plot(1:T, GIRF_I_fiscal, type="l", main="GIRF - I (Fiscal Expansionista)", xlab="Per�odo", ylab="GIRF (%)")

# Gr�ficos para pol�tica monet�ria expansionista (redu��o de r_t)
plot(1:T, GIRF_Y_monetario, type="l", main="GIRF - Y (Monet�ria Expansionista)", xlab="Per�odo", ylab="GIRF (%)")
plot(1:T, GIRF_C_monetario, type="l", main="GIRF - C (Monet�ria Expansionista)", xlab="Per�odo", ylab="GIRF (%)")
plot(1:T, GIRF_I_monetario, type="l", main="GIRF - I (Monet�ria Expansionista)", xlab="Per�odo", ylab="GIRF (%)")

# Gr�ficos para pol�tica fiscal expansionista (redu��o de Tt)
plot(1:T, GIRF_Y_impostos, type="l", main="GIRF - Y (Redu��o de Impostos)", xlab="Per�odo", ylab="GIRF (%)")
plot(1:T, GIRF_C_impostos, type="l", main="GIRF - C (Redu��o de Impostos)", xlab="Per�odo", ylab="GIRF (%)")
plot(1:T, GIRF_I_impostos, type="l", main="GIRF - I (Redu��o de Impostos)", xlab="Per�odo", ylab="GIRF (%)")


