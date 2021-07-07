
print('Insira 4 valores: ')

tupula = (int(input('Valor: ')),int(input('Valor: ')),int(input('Valor: ')),int(input('Valor: ')))

print('Valores digitados: {}'.format(tupula))
print('O valor 5 apareceu {} vezes'.format(tupula.count(5)))
if 3 in tupula:
    print('O valor 3 apareceu na posicao: {}'.format(tupula.index(3)+1))
else:
    print('Nao existe o 3')
print('Os valores pares digitados: ', end='')

for c in tupula:
    if c % 2 == 0:
        print(c, end=' ')

