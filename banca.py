#Quebrando a Banca 

endOfFile = False

#vai ter duas listas a original e a sorted

while not endOfFile:
    try:
        #leio a quantidade de caracteres e a quantidade de caracteres que eu quero retirar
        qtdCaracteres, qtdCaracteresRetirar = input().split()
        qtdCaracteres = int(qtdCaracteres)
        qtdCaracteresRetirar = int(qtdCaracteresRetirar)
        #leio a string
        string = input()
        #crio uma lista com os caracteres da string
        lista = list(string)
        #crio uma lista com os caracteres da string ordenados
        listaOrdenada = sorted(lista)
        #crio uma lista com os caracteres que eu quero retirar
        listaRetirar = listaOrdenada[:qtdCaracteresRetirar]
        #removo os caracteres que eu quero retirar da lista original
        for i in listaRetirar:
            lista.remove(i)
        #imprimo a lista original
        print(''.join(lista))
    except EOFError:
        endOfFile = True

        