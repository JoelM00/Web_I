
stop = False
acum = 0
cont = 0

while not stop:
    n = int(input('Insira um numero: '))
    if n != 999:
        acum += n
        cont += 1
    else:
        stop = True

print('Foram digitado {} numeros, somando: {}'.format(cont, acum))
