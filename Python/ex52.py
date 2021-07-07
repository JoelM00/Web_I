tupula = ('ola', 'amigo', 'queres', 'jogar', 'um', 'jogo', 'online',
          'ou', 'perferes', 'fazer', 'outra', 'cena')

for p in tupula:
    print('Na palavra: {} temos '.format(p.upper()), end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print('\033[31m{}\033[m'.format(letra), end=' ')
    print('')