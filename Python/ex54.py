valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c in range(0, 2):
    valores.append(int(input('Insira um valor: ')))

for c, v in enumerate(valores):
    print('Na posicao: {} esta o valor: {}'.format(c,v))
print('Fim')

clone = valores[:] #cria uma copia de todos os valores
clone[2] = -1
print(clone)