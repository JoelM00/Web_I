
lista = []

while True:
    val = int(input('Insira um valor: '))
    lista.append(val)
    stop = str(input('Quer continuar [s/n]? ')).strip().upper()
    if stop == 'N':
        break

print('Foram digitados: {} elementos'.format(len(lista)))
print('Lista em ordem decrescente: {}'.format(sorted(lista, reverse=True)))

if len(lista) in lista:
    print('O valor {} esta na lista'.format(len(lista)))
else:
    print('O valor {} nao esta na lista!'.format(len(lista)))