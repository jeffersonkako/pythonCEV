'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(* num):
    cont = maior = 0
    print('nalisando os valores...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')
    
        
#Programa principal
maior(2, 9, 4, 5)