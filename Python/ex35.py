
sex = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]

while sex not in 'MmFm':
    sex = str(input('Dados invalido! Digite novamente [M/F]: ')).strip().upper()[0]

print('Sexo {} registado com sucesso!'.format(sex))