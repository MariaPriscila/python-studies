n, t = map(int, input().split())

canos = []
for i in range(n):
    c, v = map(int, input().split())
    canos.append((c, v))

def combine(inp):
    return combine_helper(inp, [], [])


def combine_helper(inp, temp, ans):
    for i in range(len(inp)):
        current = inp[i]
        remaining = inp[i + 1:]
        temp.append(current)
        ans.append(tuple(temp))
        combine_helper(remaining, temp, ans)
        temp.pop()
    return ans


combinations = combine(canos)
max_valor = 0

for comb in combinations:
    combSize =0
    combPrice =0
    for pipe in comb:
        combSize+=pipe[0]
        combPrice+=pipe[1]

    if (combSize<=t and combPrice>max_valor):
        max_valor=combPrice
    
print(max_valor)
