''' Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também 
o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import *
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['Ctps'] = int(input('Carteira de trabalho: [0 não tem] '))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = int(input('Salario: '))
    dados['Aposentadoria'] =dados['Idade'] + dados['Contratação'] + 35 - datetime.now().year
    
print('='* 30)
for k, v in dados.items():
    print(f'- {k}: {v} ')
