'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
aluno['Nome'] = str(input('Nome do aluno: '))
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
aluno['Media'] = (nota1 + nota2) / 2

if aluno['Media'] >= 7.0:
    aluno['Situação'] = 'Aprovado'
elif 5.0 <= aluno['Media'] < 7.0:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
    
print('='* 30)

for k, v in aluno.items():
    print(f'- {k}: {v}')

    
    

