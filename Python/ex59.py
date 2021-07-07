
lista = []
pares = []
impares = []

while True:
    val = int(input('Insira um valor: '))
    lista.append(val)
    stop = str(input('Quer continuar [s/n]? ')).strip().upper()
    if stop == 'N':
        break

for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('Lista : {}'.format(lista))
print('Lista de pares : {}'.format(pares))
print('Lista de impares: {}'.format(impares))
