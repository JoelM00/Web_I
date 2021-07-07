
salario = int(input('Qual o seu salario: '))

if salario < 900:
    novo = salario * 1.35
else:
    novo = salario * 1.1

print('Passas a ganhar {}$ inves de {}$'.format(novo,salario))