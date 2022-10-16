'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista1 = []
for v in range(0,10):
    lista1.append(int(input('Digite um numero: ')))
print(f' O maior valor da lista foi {max(lista1)} e o menor valor lista foi {min(lista1)}')

print(lista1)

      