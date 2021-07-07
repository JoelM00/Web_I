tupula = ('CocaCola', 3.5,
          'BigMac', 4.5,
          'The Last Of Us', 70,
          'PS5', 500,
          'Gaming PC', 1000)

print('-'*40)
print(f'{"Listagem":^40}')
print('-'*40)
for item in range(0, len(tupula)):
    if item % 2 == 0:
        print(f'{tupula[item]:.<30}', end='')
    else:
        print(f'${tupula[item]:>5.2f}')
print('-'*40)