
print('Bem vindo ao Banco!')

valor = int(input('Qual o valor a levantar: '))

nota500 = 0
nota200 = 0
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
moedas1 = 0
moedas2 = 0

while valor > 0:
    if valor >= 500:
        valor -= 500
        nota500 += 1
    elif valor >= 200:
        valor -= 200
        nota200 += 1
    elif valor >= 100:
        valor -= 100
        nota100 += 1
    elif valor >= 50:
        valor -= 50
        nota50 += 1
    elif valor >= 20:
        valor -= 20
        nota20 += 1
    elif valor >= 10:
        valor -= 10
        nota10 += 1
    elif valor >= 5:
        valor -= 5
        nota5 += 1
    elif valor >= 2:
        valor -= 2
        moedas2 += 1
    else:
        valor -= 1
        moedas1 += 1

if nota500 > 0:
    print('Usou {} notas de 500'.format(nota500))
if nota200 > 0:
    print('Usou {} notas de 200'.format(nota200))
if nota100 > 0:
    print('Usou {} notas de 100'.format(nota100))
if nota50 > 0:
    print('Usou {} notas de 50'.format(nota50))
if nota20 > 0:
    print('Usou {} notas de 20'.format(nota20))
if nota10 > 0:
    print('Usou {} notas de 10'.format(nota10))
if nota5 > 0:
    print('Usou {} notas de 5'.format(nota5))
if moedas2 > 0:
    print('Usou {} moedas de 2'.format(moedas2))
if moedas1 > 0:
    print('Usou {} moedas de 1'.format(moedas1))