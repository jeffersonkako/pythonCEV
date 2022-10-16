'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]
spar = mai = scol = 0

for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
print('='*30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
        if matriz[lin][col] % 2 == 0:
            spar += matriz[lin][col]
    print()

print('='*30)
print(f'A soma dos valores pares é {spar}.')
for lin in range(0, 3):
    scol += matriz[lin][2]
print(f'A soma dos valores da 3ª coluna é {scol}.')
for col in range(0, 3):
    if col == 0:
        mai = matriz[1][col]
    elif matriz[1][col] > mai:
        mai = matriz[1][col]
print(f'O maior valor da 2ª coluna é {mai}.')
        
    
    
