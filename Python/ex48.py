
numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')

while True:
    n = int(input('Digite um numero entre 0 e 10: '))
    if 0 <= n <= 10:
        break
    else:
        print('Invalido! Tente novamente!')

print('Por extenso: {}'.format(numeros[n]))