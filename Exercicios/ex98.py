'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:     
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep

def contador(i, f, p):
    print(f ‘Con de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if 1 <f:
        cont = i
        while cont <=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = 1
        while cont >=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim')
    