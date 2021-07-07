
lista = []
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input('Insira o valor para a posicao {}: '.format(c))))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    else:
        if lista[c] < menor:
            menor = lista[c]
        elif lista[c] > maior:
            maior = lista[c]

print('Lista formada: {}'.format(lista))
print('-'*15)

print('Maior valor: {} nas posicoes: '.format(maior), end='')
for i, v in enumerate(lista):
    if v == maior:
        print('\033[31m{}\033[m'.format(i), end=' ')

print('\nMenor valor: {} nas posicoes: '.format(menor), end='')
for i, v in enumerate(lista):
    if v == menor:
        print('\033[31m{}\033[m'.format(i), end=' ')