
dicionario = {}
listagem = []
marcados = []

while True:
    nome = input('Insira o nome: ')
    partidas = int(input('Quantas partidas jogou: '))
    for i in range(partidas):
        golos = int(input('Quantos golos marcou no {} jogo: '.format(i+1)))
        marcados.append(golos)
    dicionario['nome'] = nome
    dicionario['golos'] = marcados[:]
    dicionario['total'] = sum(marcados)
    listagem.append(dicionario.copy())
    marcados.clear()
    while True:
        stop = input('Quer continuar? [S/N]: ').upper()
        if stop in 'NS':
            break
    if stop == 'N':
        break

print('-'*50)
print('cod ', end='')
for i in dicionario.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(listagem):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)

while True:
    chave = int(input('Escolha o jogador (999 stop): '))
    if chave == 999:
        break
    if chave > len(listagem):
        print('Erro!')
    else:
        print('A mostar dados de: ', listagem[chave]['nome'])
        for i, e in enumerate(listagem[chave]['golos']):
            print('Golos no jogo {}: {}'.format(i+1, e))
