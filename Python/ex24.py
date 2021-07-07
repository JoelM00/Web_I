from datetime import date

ano = int(input('Diga o ano de nascimento: '))

idade = date.today().year - ano

print('Quem nasceu em {} tem {} anos'.format(ano, idade))

if idade < 18:
    print('Vai ser listado daqui a {} anos'.format(18 - idade))
elif idade == 18:
    print('Deve fazer o alistamente este ano!')
else:
    print('Ja devia ter sido listado ha {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(ano + 18))

