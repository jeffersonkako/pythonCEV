''' Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

media1 = float(input('Digite a nota 1: '))
media2 = float(input('Digite a nota 2: '))
mediaTotal = (media1 + media2) / 2

if mediaTotal <= 5:
    print(f'Media {mediaTotal}: REPROVADO' )
elif mediaTotal <= 6.9 and  mediaTotal > 5.0: # 5.0 > mediaTotal <= 6.9 - tambem funciona
    print(f'Media {mediaTotal}: RECUPERAÇÃO' )
else:
    print(f'Media {mediaTotal}: APROVADO')
    