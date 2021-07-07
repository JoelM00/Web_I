
def maior(*numeros):
    cont = max = 0
    for valor in numeros:
        if cont == 0:
            max = valor
        else:
            if valor > max:
                max = valor
        cont += 1
    print(max)
    print('Foram mandados {} numeros!'.format(cont))

print('Analisando valores!')
print('Maior: ',end='')
maior(1,2,3,4,5,6,7)
print('Analisando valores!')
print('Maior: ',end='')
maior(1,2,354)
print('Analisando valores!')
print('Maior: ',end='')
maior(111,2,3,5)