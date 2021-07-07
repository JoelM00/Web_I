n1 = int(input('Diga um valor: '))
n2 = int(input('Diga outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
divInt = n1 // n2
exp = n1 ** n2

print('A soma vale {}'.format(s))
print('A mutiplicacao vale {}'.format(m))
print('A divisao vale {:.3f}'.format(d))
print('A divisao inteira vale {}'.format(divInt))
print('A exponenciacao vale {}'.format(exp), end=' ')
print('Repara que ficou na mesma linha')
