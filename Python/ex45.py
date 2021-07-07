from random import randint

cont = 0

while True:
    jogada = int(input('Diga um valor: '))
    pc = randint(0, 11)
    total = jogada + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]

    print('Voce jogou {} e o pc {}. Total {}'.format(jogada, pc, total))

    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            cont += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Voce venceu!')
            cont += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
print('Jogo terminado, ganhou {} vezes'.format(cont))