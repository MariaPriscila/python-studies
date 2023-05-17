#Funcao principal
def main():
    #entrada de dados
    n, m = map(int, input().split())
    #cria uma matriz com n linhas e m colunas
    tabuleiro = []
    for i in range(n):
        linha = list(input())
        tabuleiro.append(linha)

    pastos = identificaPastos(tabuleiro,n,m)
    ovelhas,lobos = calculaOvelhasLobos(pastos)
    
    print(f'{ovelhas} {lobos}')

def calculaOvelhasLobos(pastos):
    totalLobos = 0
    totalOvelhas = 0
    for pasto in pastos:
        lobos = 0
        ovelhas = 0
        for campo in pasto:
            if campo[2] == 'k':
                ovelhas += 1
                continue
            if campo[2] == 'v':
                lobos += 1
        if ovelhas > lobos :
            totalOvelhas+= ovelhas
        else:
            totalLobos+= lobos

    return totalOvelhas, totalLobos    

#Funcao para identificar os pastos
def identificaPastos(tabuleiro,n,m):
    pastos = []
    for i in range(n):
        for j in range(m):
            procuraNoPasto(tabuleiro,pastos,i+1,j+1)
    return pastos

def procuraNoPasto(tabuleiro,pastos,i,j):
    if tabuleiro[i-1][j-1] != '#':
        if not fazPartePasto(pastos,i,j):
            adicionaPartePasto(pastos, i, j, tabuleiro[i-1][j-1])
            if i != 1:
                procuraNoPasto(tabuleiro,pastos,i-1,j)
            if i != len(tabuleiro):
                procuraNoPasto(tabuleiro,pastos,i+1,j)
            if j != 1:
                procuraNoPasto(tabuleiro,pastos,i,j-1)
            if j != len(tabuleiro[i-1]):
                procuraNoPasto(tabuleiro,pastos,i,j+1)
            
def fazPartePasto(pastos, i, j):
    for pasto in pastos:
        for campo in pasto:
            if campo[0] == i and campo[1] == j:
                return True
    return False

def adicionaPartePasto(pastos, i, j, char):
    for pasto in pastos:
        for campo in pasto:
            if (campo[0] == i - 1 or campo[0] == i + 1) and campo[1] == j:
                pasto.append((i,j, char))
                return
            if campo[0] == i and (campo[1] == j - 1 or campo[1] == j + 1):
                pasto.append((i,j, char))
                return
    pastos.append([(i,j, char)])

#chama a funcao principal
main()