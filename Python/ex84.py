def notas(*notas, situacao=False):
    dicionario = {}
    dicionario['total'] = len(notas)
    dicionario['media'] = sum(notas)/len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)
    if situacao:
        if dicionario['media'] < 5:
            dicionario['situacao'] = 'Pessima'
        elif dicionario['media'] > 15:
            dicionario['situacao'] = 'Excelente'
        else:
            dicionario['situacao'] = 'Normal'
    return dicionario

'''
    cont = 0
    somatorio = 0
    maior = menor = 0
    for n in notas:
        if cont == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        cont += 1
        somatorio += n
    media = somatorio / cont
    dicionario['total'] = cont
    dicionario['media'] = media
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    
    if situacao:
        if media < 5:
            dicionario['situacao'] = 'Pessima'
        elif media > 15:
            dicionario['situacao'] = 'Excelente'
        else:
            dicionario['situacao'] = 'Normal'
    return dicionario
    '''


resp = notas(1.5, 2.5, 3.5, situacao=True)
print(resp)
resp = notas(15.5, 12.5, 19.5, situacao=True)
print(resp)