
print('Progressao aritmetica!')
print('-'*20)

n = int(input('Primeiro numero: '))
r = int(input('Razao da PA: '))

cont = 0

while cont < 10:
    print(n + r * cont, end=' -> ')
    cont += 1
print('Fim!')