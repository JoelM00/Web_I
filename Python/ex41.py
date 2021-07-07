
print('Progressao aritmetica!')
print('-'*20)

n = int(input('Primeiro numero: '))
r = int(input('Razao da PA: '))

stop = False
default = 10
acum = n
res = 0

while not stop:
    cont = 0

    while cont < default:
        print(acum, end=' -> ')
        acum += r
        cont += 1
        res += 1

    print('Pausa!')
    mais = int(input('Quantos termos quer ver mais: '))

    if mais == 0:
        stop = True
        print('Foram calculados {} termos'.format(res))
    else:
        default = mais
