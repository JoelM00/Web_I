
idadeMVelho = 0
nomeMVelho = 'None'
acum = 0
cont = 0

for c in range(1, 5):
    print('---- {} Pessoa ----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sex = str(input('Sexo[M/F]: ')).strip()
    acum += idade
    if sex == 'M':
        if nomeMVelho == 'None':
            nomeMVelho = nome
            idadeMVelho = idade
        else:
            if idade > idadeMVelho:
                idadeMVelho = idade
                nomeMVelho = nome
    else:
        if sex == 'F' and idade < 20:
            cont += 1

print('Media de idade: {}'.format(acum/4))
print('O homem mais velho: {} com {} anos'.format(nomeMVelho, idadeMVelho))
print('Existem {} mulheres com menos de 20 anos'.format(cont))