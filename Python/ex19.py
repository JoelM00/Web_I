print('-//'*10)
print('Analisador de triangulos!')
print('-//'*10)

p = int(input('Diga o primeiro segmento: '))
s = int(input('Diga o segundo segmento: '))
t = int(input('Diga o terceiro segmento: '))

if p < s + t and s < p + t and t < p + s:
    print('Os segmentos podem formar um triangulo!')
else:
    print('Os segmentos nao podem formar um triangulo!')


