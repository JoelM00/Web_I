from random import randint

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for k in range(0, 3):
        matriz[c][k] = randint(0, 10)

print(matriz)
print('Mais bonita:')

for c in range(0, 3):
    for k in range(0, 3):
        print(f'[{matriz[c][k]:^5}]', end=' ')
    print('')