print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
-=-=-=-=[Converter/Binario]=-=-=-=-
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')

def convert_bin(dec):
	bin = ''
	while dec > 0:
		bin+= str(dec%2)
		dec//= 2
	return bin[::-1]

if __name__ == '__main__':

	num = int(input("Digite um número: "))
	print("O número {} em binário é: ".format(num) +convert_bin(num))