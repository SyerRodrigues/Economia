import sympy as sp

# Definindo as variáveis e parâmetros
Y, r = sp.symbols('Y r')  # Produto (Y) e taxa de juros (r)
c0, c1, c2 = sp.symbols('c0 c1 c2')  # Parâmetros do consumo
b0, b1, b2 = sp.symbols('b0 b1 b2')  # Parâmetros do investimento
g0, t0, t1 = sp.symbols('g0 t0 t1')  # Gastos do governo e tributação
d0, d1, d2 = sp.symbols('d0 d1 d2')  # Parâmetros da demanda por moeda
M, P = sp.symbols('M P')  # Oferta de moeda e nível de preços

# Renda disponível (YD)
YD = Y - (t0 + t1 * Y)

# Consumo e Investimento
C = c0 + c1 * YD - c2 * r
I = b0 + b1 * YD - b2 * r

# Curva IS: Y = C + I + G
IS = sp.Eq(Y, C + I + g0)

# Curva LM: M/P = MD/P
LM = sp.Eq(M / P, d0 + d1 * Y - d2 * r)

# Resolvendo para o equilíbrio (Y, r)
equilibrio = sp.solve([IS, LM], (Y, r))
Y_eq, r_eq = equilibrio[Y], equilibrio[r]

# Derivadas para analisar os efeitos de g0
dY_dg0 = sp.diff(Y_eq, g0)
dC_dg0 = sp.diff(C.subs(Y, Y_eq).subs(r, r_eq), g0)
dI_dg0 = sp.diff(I.subs(Y, Y_eq).subs(r, r_eq), g0)
dr_dg0 = sp.diff(r_eq, g0)

# Resultados
print("Equilíbrio do modelo IS-LM:")
print(f"Produto de equilíbrio (Y): {Y_eq}")
print(f"Taxa de juros de equilíbrio (r): {r_eq}")

print("\nDerivadas:")
print(f"dY/dg0: {dY_dg0}")
print(f"dC/dg0: {dC_dg0}")
print(f"dI/dg0: {dI_dg0}")
print(f"dr/dg0: {dr_dg0}")

# Análise de crowding out
if dI_dg0 < 0:
    print("\nOcorre efeito crowding out: o investimento privado diminui com o aumento dos gastos do governo.")
else:
    print("\nNão ocorre efeito crowding out: o investimento privado não diminui com o aumento dos gastos do governo.")
