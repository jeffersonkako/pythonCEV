''' Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

pessoas = {}
galera = []
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while True:
        if pessoas['Sexo'] in 'MF':
            break
        else:
            print('Erro! Digite apenas M ou F')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Continuar: [S/N] ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('='*30)
print(f'(a) Foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f'(b)A media de idades foi de {media}')
print('(c) A lista de mulheres:')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}')
print('A lista de pessoas acima da media de idade:')
for p in galera:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}')
print('<<<<Encerrado>>>>')


