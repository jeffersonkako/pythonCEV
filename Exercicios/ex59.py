n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
opcao = 0

while opcao != 5:
    
    print(''' menu:
        [1] Soma
        [2] Multiplicar
        [3] Dividir
        [4] Subtrair
        [5] Sair do programa ''')
    opcao = int(input("Qual sua opção: "))
 
    if opcao == 1:
        soma = n1 + n2
        print("A soma entre as opçoes é {}".format(soma))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    
    elif opcao == 2:
        mult = n1 * n2
        print("A multipicação entre as opçoes é {}".format(mult))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        
    elif opcao == 3:
        div = n1 / n2
        print("A divisão entre as opçoes é {}".format(div))
        
    elif opcao == 4:
        sub = n1 - n2
        print("A subtração entre as opçoes é {}".format(sub))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        
    elif opcao == 5:
        print("Fim do programa")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        
    else:
        print("Escolha uma opção valida!")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

