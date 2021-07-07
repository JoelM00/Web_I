
def lerInt(msg):
    while True:
        x = input(msg)
        if x.isnumeric():
            return x
        else:
             print('\033[0;31mErro\033[m')

n = lerInt('Digite um numero: ')
print('Numero digitado: {}'.format(n))