'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista1 = []
men = 0
maior = 0
for v in range(0,10):
    lista1.append(int(input(f'Digite um numero para a posição {v}: ')))
    if v == 0:
        maior = men = lista1[v]
    else:
        if lista1[v] > maior:
            maior = lista1[v]
        if lista1[v] < men:
            men = lista1[v]
         
print(f' O maior valor da lista foi {max(lista1)} e o menor valor lista foi {min(lista1)}')

print(lista1)

      