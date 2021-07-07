
print('Conversor de numeros!')

numero = int(input('Diga um numero inteiro: '))
print('Escolha uma das bases para conversao: ')
print('[1] -> converter para Binario!')
print('[2] -> converter para Octal!')
print('[3] -> converter para Hexadecimal!')
opcao = int(input('Opcao: '))

if opcao == 1:
    print('O numero em binario: {}'.format(bin(numero)[2:]))
if opcao == 2:
    print('O numero em octal: {}'.format(oct(numero)[2:]))
if opcao == 3:
    print('O numero em hexadecimal: {}'.format(hex(numero)[2:]))
else:
    print('Opcao invalida!')

