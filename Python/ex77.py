from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.05)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.05)
            cont -= p
    print('Fim!')

print('Contagem de 1 ate 10 de 1 em 1: ')
contador(1, 10, 1)
print('Contagem de 1 ate 10 de 1 em 1: ')
contador(10, 0, 2)
print('Contagem personalizada: ')
i = int(input('Insira o inicio: '))
f = int(input('Insira o fim: '))
p = int(input('Insira o passo: '))
contador(i, f, p)

