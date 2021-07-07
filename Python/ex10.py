frase = str(input('Indroduza o seu nome: ')).strip().upper()

print('A letra "a" aparece: {}'.format(frase.count('A')))

print('A primeira letra "a" apareceu em {}'.format(frase.find("A")+1))

print('A ultima letra "a" apareceu em {}'.format(frase.rfind("A")+1))
