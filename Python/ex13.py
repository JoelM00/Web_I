velocidade = float(input('Diga a velocidade do carro: '))

if velocidade > 80:
    print("Multado em {}, excedeu em {} a velocidade limite!".format(7*(velocidade-80), (velocidade-80)))
else:
    print("Tudo otimo, continue assim!")