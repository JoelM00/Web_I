from random import randint

'''
print('Sou o teu computador!')

num = randint(0, 10)

print('Acabei de pensar num numero de 0 a 10!')

n = int(input('Em qual pensei: '))

while n != num:
    if n < num:
        print('Muito pequeno!', end=' ')
    else:
        print('Muito grande!', end=' ')
    n = int(input('Tente novamente: '))

print('Acertou! Fantastico! {} = {}'.format(num, n))
'''

pc = randint(0, 10)
print('Acabei de pensar em um numero!')
print('Qual foi?')

acertou = False
tentativas = 0

while not acertou:
    n = int(input('Valor a tentar: '))
    tentativas += 1
    if n == pc:
        acertou = True
    elif n < pc:
        print('Numero muito pequeno!')
    else:
        print('Numero muito grande!')

print('Acertou! Com {} tentativas'.format(tentativas))