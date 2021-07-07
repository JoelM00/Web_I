
stop = False

while not stop:
    num = int(input('Insira o numero: '))
    if num != 0:
        acum = 1

        print('Calculando {}! = '.format(num), end='')
        while num > 0:
            if num - 1 != 0:
                print(num, end=' x ')
            else:
                print(num, end=' ')
            acum *= num
            num -= 1

        print('= {}'.format(acum))

    else:
        stop = True
        print('Xau')