
casa = int(input('Diga o valor da casa: '))

salario = int(input('Diga o seu salario: '))

anos = int(input('Diga em quantos anos quer pagar: '))

prestMensal = casa / (anos*12)
minimo = salario * 0.3

print('Tem que pagar {} e o minimo e {}'.format(prestMensal,minimo))

if prestMensal > minimo:
    print('Rejeitado! Salario demasiado pequeno!')
else:
    print('Aceite! Ira pagar {:2f}$ por mes!'.format(prestMensal))

