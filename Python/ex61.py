teste = []
teste.append('Joel')
teste.append(21)
print(teste)

galera = []

'''
galera.append(teste) # Na lista galera ira ser colocado o apontador para teste
teste[0] = 'Maria' # Estas a subsitituir os valores iniciais
teste[1] = 40
galera.append(teste)
print(galera)
'''

galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 40
galera.append(teste[:])
print(galera)

for p in galera:
    print('{} tem {} anos'.format(p[0], p[1]))
