'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

import random
from time import sleep
from operator import itemgetter

dados = {'jogador1': random.randint(1, 6),
         'jogador2': random.randint(1, 6),
         'jogador3': random.randint(1, 6),
         'jogador4': random.randint(1, 6)}

ranking = []

print('Valores sorteados:')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('='* 30)
print('== Ranking ==')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)    
    

