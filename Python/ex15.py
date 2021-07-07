dist = int(input('Diga a distancia da viagem: '))

print('Voce vai comecar uma viagem de {}'.format(dist))

'''
if dist < 100:
    custo = 1.5*dist
else:
    custo = 0.5*dist
'''

custo = dist * 0.5 if dist <= 100 else dist*1.5
print('O custo da viagem sera: {}'.format(custo))