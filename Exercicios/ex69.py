''' Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

total18 = totalH = totalf20 = 0

while True:
    
    idade = int(input('Digite uma idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual sexo? [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 20:
        totalf20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
    
print(f'Total de pessoas acima de 18 anos foram {total18}')
print(f'Total de homens cadastrados foram {totalH}')
print(f'Total de mulheres abaixo de 20 anos foram {totalf20}')
    
        