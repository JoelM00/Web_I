
lista = []
dicionario = {}

stop = 'N'

while stop == 'N':
    nome = input('Insira o nome: ')
    while True:
        sexo = input('Insira o sexo: [M/F] ').upper()
        if sexo != 'M' and sexo != 'F':
            print('Erro! Insira novamente!')
        else:
            break
    idade = input('Insira a idade: ')
    dicionario['nome'] = nome
    dicionario['sexo'] = sexo
    dicionario['idade'] = idade
    lista.append(dicionario.copy())
    dicionario.clear()
    while True:
        continuar = input('Quer continuar? [S/N] ').upper()
        if continuar == 'N':
            stop = 'S'
            break
        elif continuar != 'S':
            print('Erro! Insira novamente!')
        else:
            break

print('-'*30)
print('Temos {} pessoas registadas'.format(len(lista)))

somatorio = 0
for l in lista:
    for k, v in l.items():
        if k == 'idade':
            somatorio += int(v)
media = somatorio/len(lista)
print('A media de idades e: {}'.format(media))

print('As mulheres registadas foram: ', end='')

for l in lista:
    if l['sexo'] == 'F':
        print(l['nome'], end=' ')
print()

print('Lista de pessoas que estao acima da media: ')
for l in lista:
    if int(l['idade']) > media:
        print(l)
