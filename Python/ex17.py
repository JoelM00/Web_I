num1 = int(input('Diga qual o numero: '))
num2 = int(input('Diga qual o numero: '))
num3 = int(input('Diga qual o numero: '))

menor = num1
#Verificar o menor
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1
#Verificar o maior
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O {} e o menor numero'.format(menor))
print('O {} e o maior numero'.format(maior))
