
def pesquisar(dicio):
    pesquisar = input('\nDigite o nome que deseja pesquisar: ').upper()
    if dicio.get(pesquisar) != None:
        lista = dicio.get(pesquisar)
        print('\n_____________________________')
        print('\nOps... numero vazado!')
        print('\033[1;91m'+'Numero.........'+'\033[0;0m', lista[0])
        print('_____________________________')
    else:
        print('\n_______________________________________________________')
        print(f'\033[1;92m\nNao foi encontrado nenhum resultado com o nome "{pesquisar}".\033[0;0m')
        print('_______________________________________________________')
    tmp = input('\033[1;93m'+'\nEnter para continuar...'+'\033[0;0m')

def cadastro(dicio):
    resp = "S"
    while resp == "S":
        nome = input("\nEntre com um nome: ").title()
        dicio[nome]= [input("Entre com um numero: ")]
        print('\n____________________________________________________')
        print(f'\033[1;92m\nNumero de "{nome}" cadastrado com sucesso! '+'\033[0;0m')
        print('____________________________________________________')
        print('\n')
        resp = input("\nDeseja cadastrar mais um numero? S ou N: ").title()

def exibir(dicio):
    for tag, lista in dicio.items():
        print("\nNome.............", tag)
        print("Numero........... ", lista[0])
        print('_____________________________')
    tmp = input('\033[1;93m'+'\nEnter para continuar...'+'\033[0;0')

def excluir(dicio):
    nome = input("\nDigite um nome que deseja excluir: ").upper()
    if dicio.get(nome) != None:
        del dicio[nome]
        print('\n____________________________________________________')
        print(f'\033[1;92m\nOs dados do nome "{nome}" foram excluidos com sucesso! '+'\033[0;0m')
        print('____________________________________________________')
    else:
        print('\n______________________')
        print('\033[1;91m'+'\n Nome não encontrado!'+'\033[0;0m')
        print('______________________')
    tmp = input('\033[1;93m'+'\nEnter para continuar...'+'\033[0;0m')