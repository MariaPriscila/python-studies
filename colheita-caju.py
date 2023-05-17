# Colheita de Caju
L, C, M, N = map(int, input().split())
cajus = [list(map(int, input().split())) for _ in range(L)]

# Calcula a soma acumulada dos valores de cajus em cada sub-retângulo
soma_acumulada = [[0] * (C + 1) for _ in range(L + 1)]
for i in range(1, L + 1):
    for j in range(1, C + 1):
        soma_acumulada[i][j] = cajus[i - 1][j - 1] + soma_acumulada[i - 1][j] + soma_acumulada[i][j - 1] - soma_acumulada[i - 1][j - 1]

# Encontra o sub-retângulo com a maior soma acumulada
max_soma = -1
for i in range(M, L + 1):
    for j in range(N, C + 1):
        soma = soma_acumulada[i][j] - soma_acumulada[i - M][j] - soma_acumulada[i][j - N] + soma_acumulada[i - M][j - N]
        max_soma = max(max_soma, soma)

# Resultado
print(max_soma)
