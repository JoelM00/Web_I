

def voto(ano):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - ano
    if idade >= 80 or 16 <= idade < 18:
        return 'Voto opcioal!'
    elif idade < 16:
        return 'Voto proibido!'
    else:
        return 'Voto obrigatorio!'



print(voto(2000))
print(voto(2020))
print(voto(1500))