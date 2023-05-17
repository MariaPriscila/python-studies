
def main():
    n = int(input())
    pilha = [int(x) for x in input().split()]
    soma = sum(pilha)
    b = (((2 * soma) / n) + (n - 1)) // 2
    a = 1 + b - n
    moves = 0
    movimentos = 0
    for i in range(n):
        moves += (pilha[i] - (i + a))
        if pilha[i] > i + a:
            movimentos += (pilha[i] - (i + a))
    if moves != 0:
        print(-1)
    else:
        print(movimentos)

main()