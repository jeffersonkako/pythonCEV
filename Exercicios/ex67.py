''' Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''




while True:
    num = int(input("Qual tabuada você quer? "))
    if num < 0:
        break
    print("-" * 20)
    for cont in range (1, 11):
        print(f"{num} x {cont} = {num*cont}")
    print("-" * 20)
print(" Acabou ")
    