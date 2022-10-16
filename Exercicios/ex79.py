''' Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []

while True:
    n = int(input('Digite um numero: '))
    
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado.')
        
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
lista.sort()
