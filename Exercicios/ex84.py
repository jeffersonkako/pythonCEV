'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
guardando tudo em uma lista. No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.'''

pessoas = []
geral = []
mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    
    if len(geral) == 0:
        mai = men = pessoas[1]
    else:
        if len(pessoas) > men:
            men = pessoas[1]
        if len(pessoas) < mai:
            mai= pessoas[1] 
                  
    geral.append(pessoas[:])
    pessoas.clear()
    
    
    resp = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break

print('='*30)   
print(geral)
print(f'Foram cadastradas {len(geral)} pessoas.')
print(f'O maior peso {mai}.')
print(f'O menor peso {men}.')