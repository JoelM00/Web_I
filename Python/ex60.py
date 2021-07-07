
expressao = str(input('Digite a expressao: '))
pilha = []

for carater in expressao:
    if carater == '(':
        pilha.append('(')
    elif carater == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')') #acontece quando n tem correspondencia!
            break

if len(pilha) == 0:
    print('Expressao correta!')
else:
    print('Expressao errada!')