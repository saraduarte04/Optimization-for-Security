from check_funcoes import*
import os

while True:
    os.system('cls')
    print('\n')
    print('\033[1;34m'+'*********************************'+'\033[0;0m')
    print('\n      BACKUP E RESTAURAÇÃO ')
    print('\033[1;34m'+'\n*********************************'+'\033[0;0m')
    print('\n')

    print('\033[1;95m'+'-------------OPCOES-------------'+'\033[0;0m')
    print('\n')
    print('1) Realizar Backup')
    print('2) Realizar Restauração')
    print('3) Sair')
    print('\n')
    perg = int(input('Selecione uma das opcoes acima: '))
    if perg == 1:
        salvar()
    elif perg == 2:
        backup()
    elif perg == 3:
        print('\033[1;92m\nObrigada!\033[0;0m')
        print('\n')
        break
    else:
        print('\n___________________')
        print('\033[1;91m'+'\n Opcao Invalida!!!'+'\033[0;0m')
        print('___________________')
        tmp = input('\033[1;93m'+'\nPrecione enter e tente novamente...'+'\033[0;0m')