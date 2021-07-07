from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['carteira'] = int(input('Carteira de trabalho (0 - n tem): '))

if dados['carteira'] != 0:
    dados['contrato'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario: '))
    dados['reforma'] = dados['idade'] + (dados['contrato'] + 35) - datetime.now().year

print('-'*30)
for k, v in dados.items():
    print(f' -> {k} tem valor {v}')