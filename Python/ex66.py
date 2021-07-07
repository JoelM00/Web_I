from random import randint

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

acumPares = 0
acumColuna = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = randint(0, 10)
        if matriz[l][c] % 2 == 0:
            acumPares += matriz[l][c]

for l in range(0, 3):
    acumColuna += matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print('')

print('Soma dos pares: {}'.format(acumPares))
print('Soma da terceira coluna: {}'.format(acumColuna))
print('Maior da segunda linha: {}'.format(maior))