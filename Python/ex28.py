
acum = 0
cont = 0

for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            acum += c
            cont = cont + 1

print('A soma de {} da: {}'.format(cont, acum))
