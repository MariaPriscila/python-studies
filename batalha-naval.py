#Funcao principal
def main():
    #entrada de dados
    n, m = map(int, input().split())
    #cria uma matriz com n linhas e m colunas
    tabuleiro = []
    for i in range(n):
        linha = list(input())
        tabuleiro.append(linha)

    #entrada de dados
    k = int(input())
    #cria uma lista com k elementos
    disparos = []
    for i in range(k):
        disparos.append([int(x) for x in list(input().split())]) 
    #print(disparos)
    navios = identificaNavios(tabuleiro,n,m)
    #print(navios)
    for i in range(len(disparos)):
        disparo = disparos[i]
        acertaNavio(disparo, navios)

    naviosDestruidos = 0
    for navio in navios:
        if len(navio) == 0:
            naviosDestruidos += 1
    print(naviosDestruidos)
    return naviosDestruidos

#Funcao para identificar os navios
def identificaNavios(tabuleiro,n,m):
    navios = []
    for i in range(n):
        for j in range(m):
            procuraNoNavio(tabuleiro,navios,i+1,j+1)
    return navios

def procuraNoNavio(tabuleiro,navios,i,j):
    if tabuleiro[i-1][j-1] == '#':
        if not existeParteNavio(navios,i,j):
            adicionaParteNavio(navios, i, j)
            if i != 1:
                procuraNoNavio(tabuleiro,navios,i-1,j)
            if i != len(tabuleiro):
                procuraNoNavio(tabuleiro,navios,i+1,j)
            if j != 1:
                procuraNoNavio(tabuleiro,navios,i,j-1)
            if j != len(tabuleiro[i-1]):
                procuraNoNavio(tabuleiro,navios,i,j+1)
            
def existeParteNavio(navios, i, j):
    for navio in navios:
        for parte in navio:
            if parte[0] == i and parte[1] == j:
                return True
    return False

#Funcao para identificar partes próximas do navio
def adicionaParteNavio(navios, i, j):
    for navio in navios:
        for parte in navio:
            if (parte[0] == i - 1 or parte[0] == i + 1) and parte[1] == j:
                navio.append((i,j))
                return
            if parte[0] == i and (parte[1] == j - 1 or parte[1] == j + 1):
                navio.append((i,j))
                return
    navios.append([(i,j)])

#Funcao acerta navio
def acertaNavio(disparo, navios):
    for navio in navios:
        for parte in navio[:]:
            if disparo[0] == parte[0] and disparo[1] == parte[1]:
                navio.remove(parte)
                return

#chama a funcao principal
main()