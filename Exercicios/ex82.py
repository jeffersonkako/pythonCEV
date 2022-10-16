'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
listaP = []
listaI = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listaP.append(v)
    else:
        listaI.append(v)
        
print('='*30)
lista.sort()
listaP.sort()
listaI.sort()
print(f'A lista completa é : {lista}')
print(f'A lista par é : {listaP}')
print(f'A lista impar é : {listaI}')
print('='*30)


