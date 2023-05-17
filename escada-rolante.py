def main():
    #entrada
    print("Digite o numero de pessoas que passaram pelo sensor: ")
    n = int(input())
    t = []
    for i in range(n):
        t.append(int(input()))
    #processamento
    tempo = 0
    for i in range(n):
        if i == 0:
            tempo += 10
        elif t[i] - t[i-1] > 10:
            tempo += 10
        else:
            tempo += t[i] - t[i-1]
    #saida
    print(tempo)

main()