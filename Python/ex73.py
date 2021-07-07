
nome = input('Nome do jogador: ')
partidas = int(input('Total de partidas: '))

dicionario = {'nome': nome}

golos = []

for i in range(partidas):
    golos.append(int(input('Quantos golos da partida {}: '.format(i))))

dicionario['golos'] = golos[:]
dicionario['total'] = sum(golos)

print(dicionario)
for k, v in dicionario.items():
    print('O campo {} tem o valor {}'.format(k,v))

print(f'O jogador {dicionario["nome"]} jogou {len(dicionario["golos"])} partidas')
for i, v in enumerate(dicionario['golos']):
    print(f' -> Na partida {i} fez {v} golos.')
print(f'Foi um total de {dicionario["total"]} golos.')
