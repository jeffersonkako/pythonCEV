''' Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
from logging import PercentStyle


total1000 = total = cont = menor = 0
barato = ' '

while True:
    produto = str(input('Nome do produto? '))
    preço = float(input('Qual preço? R$ '))
    cont += 1
    total += preço
    
    if preço > 1000:
        total1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
     
print(f'Total da compra {total}')
print(f'Quantos mais que 1000 {total1000}')
print(f'O produto mais barato é {barato} que custa {menor}')
