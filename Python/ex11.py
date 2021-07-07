nome = str(input('Diga o seu nome completo: ')).strip()

frase = nome.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome: {}'.format(frase[0]))
print('Seu ultimo nome: {}'.format(frase[len(frase)-1]))