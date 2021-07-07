
lista = []

for c in range(0, 5):
    val = int(input('Insira um valor: '))
    if c == 0 or val > lista[len(lista)-1]:
        lista.append(val)
        print('Adicionado no final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if val <= lista[pos]:
                lista.insert(pos, val)
                print('Adicionado em {}'.format(pos))
                break
            pos += 1
print('Lista: {}'.format(lista))
