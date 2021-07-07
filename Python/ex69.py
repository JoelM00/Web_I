portugal = []
estado1 = {'Localidade': 'Viana', 'Rua': 'Avenida Central'}
estado2 = {'Localidade': 'Castelo', 'Rua': 'AV. sHOPPING'}

portugal.append(estado1)
portugal.append(estado2)

print(portugal[1]['Rua'])

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print('Unidade: {} -> Sigla: {}'.format(k, v))