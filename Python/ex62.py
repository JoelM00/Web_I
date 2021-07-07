galera = []
dados = []

for c in range(0, 2):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] > 20:
        print('{} e maior de idade!'.format(p[0]))
    else:
        print('{} e menor de idade!'.format(p[0]))
