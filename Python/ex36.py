from random import randint

print('Sou o teu computador!')

num = randint(0, 10)

print('Acabei de pensar num numero de 0 a 10!')

n = int(input('Em qual pensei: '))

while n != num:
    old = num
    print('Vou voltar a pensar num numero!')
    num = randint(0, 10)
    n = int(input('Era {}! Tente novamente: '.format(old)))

print('Acertou! Fantastico! {} = {}'.format(num, n))