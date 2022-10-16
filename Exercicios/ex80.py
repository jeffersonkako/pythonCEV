'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []

for n in range (0, 6):
    v = lista.append(int(input(f'Digite um numero na posição {n}: ')))

lista.sort()
print(lista)