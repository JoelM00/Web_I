
stop = False
acum = 0
cont = 0
maior = 0
menor = 0

while not stop:
    n = int(input('Insira um numero: '))
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    acum += n
    cont += 1
    c = str(input('Quer continuar [S,N]: ')).strip().upper()
    if c == 'N':
        stop = True

print('Foram digitado {} numeros, somando: {}'.format(cont, acum))
print('Media: {} | Maior: {} | Menor: {}'.format(acum/cont, maior, menor))