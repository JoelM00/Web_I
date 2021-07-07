
lista = []

while True:
    nome = str(input('Insira o nome: ')).strip()
    nota1 = float(input('Insira a nota 1: '))
    nota2 = float(input('Insira a nota 2: '))
    media = (nota1+nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    stop = str(input('Quer continuar? [s/n]: ')).strip().upper()
    if stop == 'N':
        break

print('-'*30)
print(f'{"No.":<4}{"Nome:":<10}{"Media:":>8}')
print('-'*30)

for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 30)
    opcao = int(input('Mostrar notas de que alunos: [Sair = -1] '))
    if opcao == -1:
        print('XAU')
        break
    if opcao < len(lista) and opcao >= 0:
        print('Notas: {}'.format(lista[opcao][1]))
