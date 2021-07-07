print('\033[4;30;45mOla, mundo!\033[m')

print('\033[1;31mOla, mundo!\033[m')

a = 3
b = 5
print('Os valores sao \033[32m{}\033[m e \033[31m{}\033[m!!'.format(a, b))

nome = 'Joel'
print('Muito prazer em te conhecer, {}{}{}'.format("\033[4;34m", nome, "\033[m!!"))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))
