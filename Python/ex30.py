
n = int(input('Diga um numero: '))

cont = 0

for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print("{}".format(c), end=' ')

print('\n\033[mO num {} foi divisivel {} vezes'.format(n, cont))

if cont == 2:
    print('O numero e primo!')
else:
    print('O numero nao e primo!')