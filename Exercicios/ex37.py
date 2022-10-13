'''
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

num = int(input('Digite um número inteiro: '))
print(''' Escolha uma opção de conversão:
      [1] BINÁRIO
      [2] OCTAL
      [3] HEXADECIMAL ''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print('O número {} convertido em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} convertido em OCTAL é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} convertido em BINÁRIO é {}'.format(num, hex(num)[2:]))
else:
     print('Opção invalida')
     
