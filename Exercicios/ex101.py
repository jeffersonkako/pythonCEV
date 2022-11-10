'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
    retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

from datetime import datetime


def voto(ano):
    from datetime import date
    atual = datetime.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} voto opcional!'
    else:
        return f'Com {idade} voto obrigatório'
    
ano = int(input('Qual seu ano de nascimento: '))
print(voto(ano))
          
