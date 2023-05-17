def quickSort(countries, low, high):
    if low < high:
        pi = partition(countries, low, high)
        quickSort(countries, low, pi-1)
        quickSort(countries, pi+1, high)

def partition(countries, low, high):
    pivot = countries[high]
    i = low - 1
    for j in range(low, high):
        if countries[j][1][0] > pivot[1][0]:
            i += 1
            countries[i], countries[j] = countries[j], countries[i]
        elif countries[j][1][0] == pivot[1][0]:
            if countries[j][1][1] > pivot[1][1]:
                i += 1
                countries[i], countries[j] = countries[j], countries[i]
            elif countries[j][1][1] == pivot[1][1]:
                if countries[j][1][2] > pivot[1][2]:
                    i += 1
                    countries[i], countries[j] = countries[j], countries[i]
                elif countries[j][1][2] == pivot[1][2]:
                    if countries[j][0] < pivot[0]:
                        i += 1
                        countries[i], countries[j] = countries[j], countries[i]
    countries[i + 1], countries[high] = countries[high], countries[i + 1]
    return i + 1

def main():
    n, m = map(int, input().split())
    countries = [[i + 1, [0, 0, 0]] for i in range(n)]
    for i in range(m):
        gold, silver, bronze = map(int, input().split())
        countries[gold - 1][1][0] += 1
        countries[silver - 1][1][1] += 1
        countries[bronze - 1][1][2] += 1
    quickSort(countries, 0, n - 1)
    for i in range(n):
        print(countries[i][0], end=' ')
    print()

main()
