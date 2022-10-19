cadastroF = []
cadastroT = []
temp = {}
idF = idT = 0
def cadastroFerramentas(choice):
    temp['id'] = idF
    temp['Ferramenta'] = str(input('Ferramenta: '))
    temp['Fabricante'] = str(input('Fabricante: '))
    temp['Voltagem de Uso:'] = str(input('Voltagem de Uso: '))
    temp['Part Number'] = str(input('Part Number: '))
    temp['Tamanho:'] = str(input('Tamanho: '))
    temp['Unidade de Medida'] = str(input('Unidade de Medida: '))
    temp['Tipo de Ferramenta'] = str(input('Tipo de Ferramenta: '))
    temp['Material da Ferramenta'] = str(input('Material da Ferramenta: '))
    temp['Tempo Maximo de Reserva'] = str(input('Tempo Maximo de Reserva: '))
    cadastroF.append(temp.copy())
    temp.clear()
    print(cadastroF)
def cadastroTecnicos(choice):
    temp['id'] = idT
    temp['Nome'] = str(input('Nome: '))
    temp['Cpf'] = str(input('Cpf: '))
    temp['Contato:'] = str(input('Telefone: '))
    temp['Turno'] = str(input('Turno: '))
    temp['Equipe:'] = str(input('Equipe: '))
    cadastroT.append(temp.copy())
    temp.clear()
    print(cadastroT)
while True:
    print('=' * 30)
    choice = int(input('[MENU] \n[1] Cadastro de Ferramentas \n[2] Cadastro de Técnicos\n[3] Sair\n>>> '))
    while choice < 1 or choice > 5:
        print('=' * 30)
        print('Valor Incorreto, Digite Novamente.')
        choice = int(input('[MENU] \n[1] Cadastro de Ferramentas \n[2] Cadastro de Técnicos\n[3] Sair\n>>> '))
    if choice == 1:
        idF += 1
        cadastroFerramentas(choice)
    if choice == 2:
        idT += 1
        cadastroTecnicos(choice)
    if choice == 3:
        break
    
