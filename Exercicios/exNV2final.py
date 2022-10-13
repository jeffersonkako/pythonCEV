print('''=-=-=-= Conversor =-=-=-=
[Decimal] para [Binario]
=-=-=-=-=-=-=-=-=-=-=-=-=''')

def convert_bin(n):
    binario = '.'
    parte_dec = n
    while n != 1.0:
        n = 2*parte_dec
        parte_dec = n - int(n)
        binario += str(int(n))
    return binario

if __name__ == '__main__':
	num = float(input("Digite um número Decimal: "))
	print("O número em binário é: "+convert_bin(num))