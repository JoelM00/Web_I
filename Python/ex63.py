
lista = []
aux = []
maior = 0
menor = 0

while True:
    aux.append(str(input('Insira o nome: ')))
    aux.append(int(input('Insira o peso: ')))
    if len(lista) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]
        elif aux[1] < menor:
            menor = aux[1]
    lista.append(aux[:])
    aux.clear()
    stop = str(input('Quer continuar? [s/n]: ')).strip().upper()
    if stop == 'N':
        break

print('Lista inserida: '.format(lista))

print('Maior peso: {} corresponde a: '.format(maior), end='')

for p in lista:
    if p[1] == maior:
        print(p[0], end=' ')

print('\nMenor peso: {} corresponde a: '.format(menor), end='')

for p in lista:
    if p[1] == menor:
        print(p[0], end=' ')
