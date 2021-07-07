
print('-'*15)
print('Sequencia de Fibonacci')
print('-'*15)

max = int(input('Quantos termos quer ver: '))
print('~'*15)

t1 = 0
t2 = 1

cont = 0

penultimo = t1
ultimo = t2

print('{} -> {}'.format(t1, t2), end='')
while cont < max - 2:
    prox = ultimo + penultimo
    penultimo = ultimo
    ultimo = prox
    print(' -> {}'.format(prox), end='')
    cont += 1
print(' -> Fim!')