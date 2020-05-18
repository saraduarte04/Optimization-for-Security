from funcoes_17_05 import *
import os

dic_num = {'ALBERICO':['943607291'], 'SARA':['979901657'], 'LUCAS':['966478419'], 'JULIA':['978042624'], 'JONATHAN':['940848848'], 'NICOLAS':['914740487'], 'HENRIQUE':['938290200'], 'RAFAEL':['927182276'], 'JOSE':['961862236'], 'DAVI':['975008938'], 'TIAGO':['959682538'], 'JONAS':['968664851'], 'CLEITON':['985713324'], 'JACARE':['917013906'], 'SILVIO':['980187043'], 'ANDRE':['929637109'], 'FERNANDO':['931952663'], 'RENATO':['964573691'], 'DANTE':['996749612'], 'FELIPE':['933487573'], 'MARGARIDA':['940246703'], 'MARIA':['963202877'], 'THAIS':['938081420'], 'ROBSON':['987562686'], 'NATASHA':['957663983'], 'RENAN':['961944853'], 'OLAVO':['995014770'], 'LEANDRO':['939765421'], 'ANTONIO':['910147231'], 'DAVID':['916116618'], 'JONY':['996190176']}

while True:
    os.system('cls')
    print('\n')
    print('\033[1;34m'+'*********************************'+'\033[0;0m')
    print('\n VERIFICACAO DE NUMEROS EXPOSTOS ')
    print('\033[1;34m'+'\n*********************************'+'\033[0;0m')
    print('\n')

    print('\033[1;95m'+'-------------OPCOES-------------'+'\033[0;0m')
    print('\n')
    print('1) Pesquisar por Nome')
    print('2) Cadastrar Numero')
    print('3) Exibir numeros')
    print('4) Excluir')
    print('5) Sair')
    print('\n')
    perg = int(input('Selecione uma das opcoes acima: '))
    if perg == 1:
        pesquisar(dic_num)
    elif perg == 2:
        cadastro(dic_num)
    elif perg == 3:
        exibir(dic_num)
    elif perg == 4:
        excluir(dic_num)
    elif perg == 5:
        print('\033[1;92m\nObrigada!\033[0;0m')
        print('\n')
        break
    else:
        print('\n___________________')
        print('\033[1;91m'+'\n Opcao Invalida!!!'+'\033[0;0m')
        print('___________________')
        tmp = input('\033[1;93m'+'\nPrecione enter e tente novamente...'+'\033[0;0m')
    