lanche = ('Hamburguer', 'CocaCola', 'Pizza', 'Pudim')
# Tuplas sao imutaveis!

print(lanche[1])
print(lanche[-2])
print(lanche[1:3]) # ignora o 3
print(lanche[2:])
print(lanche[:2]) # ele ignora o elemento 2
print(lanche[-2:]) # comeca na Pizza e vai ate ao final

for comida in lanche:
    print(comida, end=' ')
print('')

for cont in range(0, len(lanche)):
    print(lanche[cont], end=' ')
print('')

for pos, comida in enumerate(lanche):
    print('Comida: {} esta na posicao: {}'.format(comida, pos))

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 6, 1, 2)
c = a+b
print(b)
print(c)

print(c.count(5)) # quantos 5 existem
print(c.index(2))
