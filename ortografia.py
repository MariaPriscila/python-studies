def distancia(a, b):
    """Função que calcula a distância entre as strings a e b."""
    m, n = len(a), len(b)
    
    # cria matriz com as distâncias mínimas
    d = [[0 for j in range(n+1)] for i in range(m+1)]
    
    # inicializa primeira coluna e linha com distâncias conhecidas
    for i in range(1, m+1):
        d[i][0] = i
    for j in range(1, n+1):
        d[0][j] = j
        
    # preenche matriz com as distâncias mínimas
    for j in range(1, n+1):
        for i in range(1, m+1):
            if a[i-1] == b[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
                
    return d[m][n]

# lê o número de palavras no dicionário e o número de palavras a serem analisadas
n, m = map(int, input().split())

# lê as palavras do dicionário
dicionario = []
for i in range(n):
    dicionario.append(input())

# lê as palavras a serem analisadas
palavras = []
for i in range(m):
    palavras.append(input())

# encontra todas as palavras do dicionário que estão a uma distância de no máximo 2 de cada palavra a ser analisada
respostas = []
for palavra in palavras:
    resposta = []
    for d in dicionario:
        if distancia(palavra, d) <= 2:
            resposta.append(d)
    respostas.append(resposta)

# imprime as respostas
for r in respostas:
    print(' '.join(r))