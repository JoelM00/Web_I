
def trata(n='Desconhecido', g=0):
    print('O jogador {} fez {} golos.'.format(n, g))

nome = input('Insira o nome: ')
golos = input('Numero de golos: ')

if golos.isnumeric():
    golos = int(golos)
else:
    golos = 0
if nome.strip() == '':
    trata(g=golos)
else:
    trata(nome, golos)