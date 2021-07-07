from random import randint

print('Jogo do Pedra/Papel/Tesoura')
print('Opcoes:')
print('[1] -> Pedra')
print('[2] -> Papel')
print('[3] -> Tesoura')
escolha = int(input('Escolha: '))

jogadas = ['Pedra', 'Papel', 'Tesoura']

jogadaPC = randint(1, 3)

if jogadaPC == 1 and escolha == 2 or jogadaPC == 2 and escolha == 3 or jogadaPC == 3 and escolha == 1:
    print('User vence! PC: {} User: {}'.format(jogadas[jogadaPC-1], jogadas[escolha-1]))
elif jogadaPC == 1 and escolha == 3 or jogadaPC == 2 and escolha == 1 or jogadaPC == 3 and escolha == 2:
    print('PC vence! PC: {} User: {}'.format(jogadas[jogadaPC-1], jogadas[escolha-1]))
else:
    print('Empate! PC: {} User: {}'.format(jogadas[jogadaPC-1], jogadas[escolha-1]))
