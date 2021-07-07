from random import randint
from time import sleep

print('Vou pensar num numero entre 0 e 5. Adivinha qual!')

rand = randint(0, 5)

num = int(input('Diga o numero: '))

print('Processando')
sleep(3)

if num == rand:
    print('Acertou, com: {}'.format(num))
else:
    print('Errou, era: {}'.format(rand))