
frase = str(input('Diga uma frase: ')).strip().upper()

'''
print('Frase inversa: ', end=' ')
for c in range(len(frase)-1, -1, -1):
    print("{}".format(frase[c]), end='')
'''

palavras = frase.split()
junto = ''.join(palavras) #eliminar os espacos
inverso = junto[::-1]

''' Aquela expressao do inverso consegue fazer isto!
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
    '''
print('O inverso de {} e {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palindrome!')
else:
    print('A frase nao e um palindrome!')