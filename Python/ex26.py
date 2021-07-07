
for c in range(1, 6):
    print(c)
print('Fim!')

for c in range(6, 1, -1):
    print(c)
print('Fim!')

n = int(input('Diga um numero: '))
incremento = int(input('Diga o incremento: '))

for c in range(0, n, incremento):
    print(c)