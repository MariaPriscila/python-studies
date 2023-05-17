def main():
    n = int(input())
    linha = list(map(int, input().strip().split()))
    sums = 0
    for x in range(n):
        num1 = linha[x]
        for y in range(x+1,n):
            num2 = linha[y]
            if num1 > num2:
                sums +=1

    print(sums)
    
main()