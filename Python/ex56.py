
lista = []
maior = 0
menor = 0

while True:
    val = int(input('Insira um valor: '))
    if val not in lista:
        lista.append(val)
    else:
        print('Valor repetido!')
    stop = str(input('Quer continuar [s/n]? ')).strip().upper()
    if stop == 'N':
        break

print('Lista: {}'.format(sorted(lista)))


