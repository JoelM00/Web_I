'''
acum = 0

for c in range(1, 7):
    n = int(input('Diga um numero inteiro: '))
    if n % 2 == 0:
        acum += n

print('A soma dos numero pares: {}'.format(acum))
'''

print('Progressao aritmetica: ')
inicio = int(input('Diga qual o inicio: '))
razao = int(input('Diga qual a razao: '))

numTermos = inicio + 10 * razao

for c in range(inicio, numTermos, razao):
    print(c,end=' -> ')
print('Fim!')