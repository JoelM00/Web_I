from time import sleep

for c in range(10, 0, -1):
    sleep(0.2)
    print(c)
print('Fim!')

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Fim!')