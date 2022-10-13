'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint

v = 0

while True:   
    jogador = int(input("Digite seu numero Jogador: "))
    computador = randint (0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar [P/I] ? ")).strip().upper()[0]
        print(f"Jogador -> {jogador} e Computador -> {computador}, total = {total} >>> ", end =" ")
        print("Deu PAR" if total % 2 == 0 else "Deu IMPAR")
        if tipo == "P":
            if total % 2 == 0:
                print("Você VENCEU!!")
                v += 1
            else:
                print("Você PERDEU!")
                break
        if tipo == "I":
            if total % 2 == 1:
                print("Você VENCEU!!")
                v += 1
            else:
                print("Você PERDEU!")
                break
        print("Vamos jogar novamente ...")
print(f"GameOver, você venceu {V} vezes!")


