tupulo = (2, 4, 5, 7, 5)
print(tupulo)

lista = [5, 3, 2, 6, 8]
print(lista)
lista[2] = 1000
lista.append(5000)
lista.sort(reverse=True)
print(lista)
print('A lista tem tamanho: {}'.format(len(lista)))
lista.insert(2, -1)
lista.pop(0)
if 8 in lista:
    lista.remove(8)
else:
    print('Nao havia nenhum 8!')
print(lista)