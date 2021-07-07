from datetime import date

menor = 0
maior = 0

for c in range(1, 8):
    nasc = int(input('Em que ano nasceu a pessoa: '))
    idade = date.today().year - nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1

print('Temos {} menores e {} maiores!'.format(menor, maior))
