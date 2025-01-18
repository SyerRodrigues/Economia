# Definindo os parâmetros
c0 = 15
c1 = 0.8
A = 15
ir = 0.5
m0 = 6
m1 = 0.03
m2 = 0.5

# Cenário base
M = 25
P = 5
G = 20
T = 20

# Função para calcular Y, r, C e I
def calcular_economias(M, P, G, T):
    # Inicializando variáveis
    r = 0  # Taxa de juros inicial
    Y = 0  # Produto inicial

    # Iterando para encontrar o equilíbrio
    for _ in range(1000):  # Limitar a 1000 iterações para evitar loops infinitos
        C = c0 + c1 * (Y - T)
        I = A - ir * r
        Y = C + I + G
        
        # Calcular a taxa de juros
        r = (M / P - m0 - m1 * Y) / m2

    return Y, r, C, I

# Cenário base
Y_base, r_base, C_base, I_base = calcular_economias(M, P, G, T)

print("Cenário Base:")
print(f"Produto (Y): {Y_base:.2f}")
print(f"Taxa de Juros (r): {r_base:.2f}")
print(f"Consumo (C): {C_base:.2f}")
print(f"Investimento (I): {I_base:.2f}")

# Cenário com aumento dos gastos públicos (G' = 40)
G_novo = 40
Y_novo, r_novo, C_novo, I_novo = calcular_economias(M, P, G_novo, T)

print("\nCenário com G' = 40:")
print(f"Produto (Y): {Y_novo:.2f}")
print(f"Taxa de Juros (r): {r_novo:.2f}")
print(f"Consumo (C): {C_novo:.2f}")
print(f"Investimento (I): {I_novo:.2f}")

# Cenário com aumento da oferta de moeda (M' = 30)
M_novo = 30
Y_novo_moeda, r_novo_moeda, C_novo_moeda, I_novo_moeda = calcular_economias(M_novo, P, G, T)

print("\nCenário com M' = 30:")
print(f"Produto (Y): {Y_novo_moeda:.2f}")
print(f"Taxa de Juros (r): {r_novo_moeda:.2f}")
print(f"Consumo (C): {C_novo_moeda:.2f}")
print(f"Investimento (I): {I_novo_moeda:.2f}")