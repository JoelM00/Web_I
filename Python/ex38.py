
stop = False

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

while not stop:
    print('[1] -> Somar')
    print('[2] -> Multiplicar')
    print('[3] -> Maior')
    print('[4] -> Novos Numeros')
    print('[5] -> Sair')
    op = int(input('Escolha: '))

    if op == 1:
        print('Soma: {}'.format(valor1+valor2))
    elif op == 2:
        print('Multiplicacao: {}'.format(valor1*valor2))
    elif op == 3:
        if valor1 > valor2:
            print('Maior: {}'.format(valor1))
        else:
            print('Maior: {}'.format(valor2))
    elif op == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif op == 5:
        stop = True
        print('Xau')
    else:
        print('Invalido!')