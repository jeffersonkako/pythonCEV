''' Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

from datetime import date

Ano_Atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = Ano_Atual - nascimento

if idade <= 9 :
    print(f'{idade} Anos = MIRIM')
elif idade <= 14 :
    print(f'{idade} Anos = INFANTIL')
elif idade <= 19 :
    print(f'{idade} Anos = JUNIOR ')
elif idade <= 25 :
    print(f'{idade} Anos = SENIOR')
else:
    print(f'{idade} Anos = MASTER')
    