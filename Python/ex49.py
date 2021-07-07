from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Sorteados o valor {}'.format(n))

print('Valores sorteados: ',end='')
for num in n:
    print(num, end=' ')

print('\nO maior valor foi: {}'.format(max(n)))
print('O menor valor foi: {}'.format(min(n)))
