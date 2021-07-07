nome = input('Diga o seu nome:')

print('O seu nome em MAISCULAS: {}'.format(nome.upper()))
print('O seu nome em minusculas: {}'.format(nome.lower()))
print('O nome completo tem: {}'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem: {}'.format(nome.find(' ')))

separa = nome.split()
print('O primeiro nome tem: {}'.format(len(separa[0])))