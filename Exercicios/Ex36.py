'''
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor = float(input(' Qual o valor da casa? R$: '))
salario = float(input(' Qual seu salário? R$: '))
anos = float(input(' Quantos anos deseja pagar? '))
minimo = salario * 30 / 100
parcela = salario / (anos * 12)
print(' Para comprar uma casa em {} anos, com o salário de {} a parcela fica: {}' .format(anos, salario, parcela))

if parcela <= minimo :
    print(' Aprovado ')
else:
    print('Negado')