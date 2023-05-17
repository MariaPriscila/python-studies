def main():
    n = int(input())
    matriz = []
    for _ in range(n):
        linha = input().split()
        matriz.append(linha)
    
    somaLinhas = []
    somaColunas = []
    for x in range(n):
        sumRow = 0
        sumCol = 0
        for y in range(n):
            sumRow += int(matriz[x][y])    
            sumCol += int(matriz[y][x])    
        somaLinhas.append(sumRow)
        somaColunas.append(sumCol)

    diffX, mostCommon = diff(somaLinhas)
    diffY,_= diff(somaColunas)

    totalSum = 0
    for y in range(n):
        if y != diffY:
            totalSum += int(matriz[diffX][y])
        
    wrongNumber = int(matriz[diffX][diffY])
    missingNumber = abs(mostCommon - totalSum)
    print(f'{missingNumber} {wrongNumber}')


def diff(arr):
    if arr[0] == arr[1] and arr[0] != arr[2]:
        return 2, arr[0]
    if arr[0] == arr[2] and arr[0] != arr[1]:
        return 1, arr[0]
    if arr[1] == arr[2] and arr[0] != arr[1]:
        return 0, arr[1]
 
    for i in range(3, len(arr)):
        if arr[i] != arr[i - 1]:
            return i, arr[i - 1]


main()