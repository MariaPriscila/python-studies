#Calculadora improvisada

# Função que realiza a soma de dois números
def soma(a, b):
    if b == 0:
        return a
    else:
        return soma(a + 1, b - 1)

# Função que realiza a multiplicação de dois números
def mult(a, b):
    if b == 0:
        return 0
    else:
        return soma(a, mult(a, b - 1))

# Função que realiza a exponenciação de dois números
def exp(a, b):
    if b == 0:
        return 1
    else:
        return mult(a, exp(a, b - 1))

# Função que realiza o sucessor de um número
def suc(a):
    return a + 1

# Função que realiza a operação de acordo com a entrada
def operacao(entrada):
    if entrada[0] == "Suc":
        return suc(int(entrada[1]))
    elif entrada[0] == "Soma":
        return soma(int(entrada[1]), int(entrada[2]))
    elif entrada[0] == "Mult":
        return mult(int(entrada[1]), int(entrada[2]))
    elif entrada[0] == "Exp":
        return exp(int(entrada[1]), int(entrada[2]))

# Função principal
def main():
    # Entrada de dados
    entrada = input().split()
    # Imprime o resultado da operação
    print(operacao(entrada))

# Chamada da função principal
main()
