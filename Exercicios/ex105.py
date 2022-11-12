'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
 '''

def notas(*n, sit=False):
    """
    Ajuda
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >=5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r


#Programa

resp = notas(5.5, 2.5, 1.5, 10, sit=True)
print(resp)
help(notas)