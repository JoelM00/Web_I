from random import randint

lista = []

def soma(l):
    somatorio = 0
    for e in l:
        if e % 2 == 0:
            somatorio += e
    print(somatorio)

def preenche(l):
    for i in range(5):
        num = randint(0, 20)
        l.append(num)
        print(num, end=' ')
    print()

print('Preenchendo lista: ',end='')
preenche(lista)

print('Soma dos pares: ', end='')
soma(lista)