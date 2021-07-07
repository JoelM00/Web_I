from random import randint

lista = list()
jogos = list()

print('Jogo Mega Cena')

num = int(input('Quantos jogos sao para sortear: '))

for c in range(0, num):
    cont = 0
    while cont < 6:
        valor = randint(0, 10)
        if valor not in lista:
            lista.append(valor)
            cont += 1
    print('Jogo {}: {}'.format(c+1, lista))
    jogos.append(lista[:])
    lista.clear()

print('Good Luck!')
print('Jogos: {}'.format(jogos))
